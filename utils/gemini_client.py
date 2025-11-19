import os
import json
import streamlit as st
from google import genai


MODEL = "gemini-2.0-flash"

BASE_SYSTEM_INSTRUCTION = """
You are a compassionate, non-judgmental, and supportive mental wellness companion. 
Your primary role is to listen empathetically, validate feelings, and provide evidence-based mental health support, 
such as guided journaling, CBT principles, and breathing exercises.
ALWAYS prioritize user safety. If the user expresses thoughts of self-harm or suicide,
immediately and gently pivot to providing the crisis resources already listed in the prompt.
NEVER provide diagnosis or claim to be a human professional.
Keep responses concise, warm, and focused on the user's emotional state.
"""

CRISIS_INSTRUCTION = """
You are a highly sensitive and empathetic crisis detection AI.
Analyze the user's message for themes related to self-harm, suicidal ideation,
severe distress, or abuse.

Your response MUST be a single JSON object:
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

        try:
            self.client = genai.Client(api_key=api_key)
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Gemini client: {e}")

    # ------------------------------------------------------
    # INTERNAL WRAPPER USING NEW CHAT COMPLETIONS ENDPOINT
    # ------------------------------------------------------
    def _chat(self, system_instruction, user_message, response_json=False):
        try:
            response = self.client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": user_message}
                ],
                response_format={"type": "json_object"} if response_json else None
            )

            return response.choices[0].message["content"]

        except Exception as e:
            import traceback
            err = traceback.format_exc()

            st.error("🔥 GEMINI API ERROR")
            st.code(err)

            print("GEMINI ERROR:", err)
            return None

    # ------------------------------------------------------
    # NORMAL CHAT REPLY
    # ------------------------------------------------------
    def get_empathetic_response(self, user_input, persona, conversation_history):
        personas = {
            "peer": "Respond like a supportive friend your age.",
            "mentor": "Respond like a guiding, encouraging mentor.",
            "therapist": "Respond like a gentle therapist (no diagnoses)."
        }

        persona_text = personas.get(persona, personas["therapist"])

        # Create a linear chat transcript
        chat_text = ""
        for msg in conversation_history:
            chat_text += f"{msg['role'].upper()}: {msg['content']}\n"

        chat_text += f"USER: {user_input}"

        full_instruction = BASE_SYSTEM_INSTRUCTION + "\n\n" + persona_text

        reply = self._chat(full_instruction, chat_text)
        return reply or "I'm here for you. Could you share a bit more?"

    # ------------------------------------------------------
    # JSON: CBT INSIGHT
    # ------------------------------------------------------
    def generate_cbt_insight(self, thought_record: dict) -> dict:
        user_msg = (
            "Analyze this thought record and return ONLY a JSON object with:\n"
            "cognitive_distortions, balanced_thoughts, encouragement.\n\n"
            + json.dumps(thought_record, indent=2)
        )

        raw = self._chat(
            system_instruction="You are a CBT analysis tool.",
            user_message=user_msg,
            response_json=True
        )

        try:
            return json.loads(raw)
        except:
            return {"error": "Failed to parse CBT JSON."}

    # ------------------------------------------------------
    # JSON: Journal Prompt
    # ------------------------------------------------------
    def generate_personalized_journal_prompt(self, mood_context, recent_themes):
        user_msg = (
            "Generate a JSON object with 'prompt' and 'follow_up_questions'.\n\n"
            f"Mood context: {json.dumps(mood_context, indent=2)}\n"
            f"Recent themes: {recent_themes}"
        )

        raw = self._chat(
            system_instruction="You create journal prompts for wellness.",
            user_message=user_msg,
            response_json=True
        )

        try:
            return json.loads(raw)
        except:
            return {"error": "Failed to parse journal prompt JSON."}

    # ------------------------------------------------------
    # JSON: Crisis Detection
    # ------------------------------------------------------
    def analyze_text_for_crisis(self, user_input: str):
        raw = self._chat(
            system_instruction=CRISIS_INSTRUCTION,
            user_message=f"User message: {user_input}",
            response_json=True
        )

        try:
            return json.loads(raw)
        except Exception:
            return {
                "risk_level": "MODERATE",
                "keywords_detected": [],
                "analysis": "Could not parse AI JSON."
            }
