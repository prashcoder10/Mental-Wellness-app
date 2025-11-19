# utils/gemini_client.py

import os
import json
import streamlit as st
import google.generativeai as genai


MODEL = "gemini-2.0-flash"

BASE_SYSTEM_INSTRUCTION = """
You are a compassionate, non-judgmental, and supportive mental wellness companion.
Your role is to listen empathetically, validate feelings, and offer grounding,
journaling, CBT reflections and emotional support.

You must NEVER give medical advice, diagnose, or pretend to be a human professional.
Always prioritize safety, be warm, concise, and emotionally validating.
"""

CRISIS_INSTRUCTION = """
You are a crisis risk analysis AI.

Return ONLY a JSON object:
{
 "risk_level": "LOW | MODERATE | HIGH | SEVERE",
 "keywords_detected": [],
 "analysis": "short reasoning"
}
"""


class GeminiClient:
    def __init__(self):
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise EnvironmentError("❌ GEMINI_API_KEY not set.")

        # Configure new Gemini SDK (2025 syntax)
        genai.configure(api_key=api_key)

        # Load model
        self.model = genai.GenerativeModel(MODEL)

    # ---------------------------------------------
    # INTERNAL WRAPPER (new correct Gemini call)
    # ---------------------------------------------
    def _generate(self, prompt, json_output=False):
        try:
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "response_mime_type": "application/json"
                    if json_output else "text/plain"
                }
            )

            # Extract text safely
            if json_output:
                return response.text  # JSON text
            else:
                return response.text  # Normal text

        except Exception as e:
            st.error("🔥 Gemini API Error")
            st.code(str(e))
            print("GEMINI ERROR:", e)
            return None

    # ------------------------------------------------------
    # NORMAL CHAT REPLY (fixed for new API)
    # ------------------------------------------------------
    def get_empathetic_response(self, user_input, persona, conversation_history):
        personas = {
            "peer": "Respond like a warm, supportive peer listener.",
            "mentor": "Respond like a kind, encouraging mentor.",
            "therapist": "Respond like a gentle therapeutic companion (no diagnosis)."
        }

        persona_text = personas.get(persona, personas["therapist"])

        # Build conversation transcript
        chat_text = ""
        for msg in conversation_history[-10:]:  # limit context to 10 messages
            chat_text += f"{msg['role'].upper()}: {msg['content']}\n"

        chat_text += f"USER: {user_input}"

        full_prompt = f"""
{BASE_SYSTEM_INSTRUCTION}

Persona style: {persona_text}

Conversation history:
{chat_text}

Respond empathically, briefly, and safely.
"""

        reply = self._generate(full_prompt)
        return reply or "I'm here with you — could you share more about how you're feeling?"

    # ------------------------------------------------------
    # JSON: CBT Insight
    # ------------------------------------------------------
    def generate_cbt_insight(self, thought_record: dict) -> dict:
        prompt = f"""
Return a JSON object with ONLY:
- cognitive_distortions
- balanced_thoughts
- encouragement

Here is the user's CBT thought record:
{json.dumps(thought_record, indent=2)}
"""

        raw = self._generate(prompt, json_output=True)

        try:
            return json.loads(raw)
        except:
            return {"error": "Failed to parse CBT JSON."}

    # ------------------------------------------------------
    # JSON: Journal Prompt Generation
    # ------------------------------------------------------
    def generate_personalized_journal_prompt(self, mood_context, recent_themes):
        prompt = f"""
Return a JSON object with:
- prompt
- follow_up_questions

Mood context:
{json.dumps(mood_context, indent=2)}

Themes: {recent_themes}
"""

        raw = self._generate(prompt, json_output=True)

        try:
            return json.loads(raw)
        except:
            return {"error": "Failed to parse journal prompt JSON."}

    # ------------------------------------------------------
    # JSON: Crisis Detection Model
    # ------------------------------------------------------
    def analyze_text_for_crisis(self, user_input: str):
        prompt = f"{CRISIS_INSTRUCTION}\n\nUser message: {user_input}"

        raw = self._generate(prompt, json_output=True)

        try:
            return json.loads(raw)
        except:
            return {
                "risk_level": "MODERATE",
                "keywords_detected": [],
                "analysis": "Could not parse AI JSON."
            }
