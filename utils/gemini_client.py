# utils/gemini_client.py

import os
import json
import streamlit as st  # added import
from google import genai
from google.genai import types

# Define the model to use
MODEL = 'gemini-2.5-flash'

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
You are a highly sensitive and empathetic crisis detection AI. Analyze the user's message 
for themes related to self-harm, suicidal ideation, severe distress, or abuse.
Your response MUST be a single JSON object.
Risk Levels are: LOW, MODERATE, HIGH, SEVERE. 
Focus your detection on identifying the presence of immediate danger or clear plans for self-harm.
"""

class GeminiClient:
    def __init__(self):
        """Initialize Gemini client; raise if API key not configured."""
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            # avoid calling st.error in library initialization — raise so caller can handle/display
            raise EnvironmentError("GEMINI_API_KEY not found in environment. Set GEMINI_API_KEY.")
        # Initialize client (SDK should read env key or you may need to pass it explicitly)
        try:
            self.client = genai.Client()
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Gemini client: {e}")

    def _generate_content(self, model_name: str, contents, system_instruction: str, is_json: bool = False):
        """Helper function to call the Gemini API. Returns the raw response object."""
        if not hasattr(self, "client") or self.client is None:
            raise Exception("Gemini client is not initialized. Check GEMINI_API_KEY.")
        
        config_params = {
            "system_instruction": system_instruction,
            "temperature": 0.7 if not is_json else 0.0,
        }
        if is_json:
            config_params["response_mime_type"] = "application/json"

        # The SDK surface may differ — wrap in try/except and return object
        try:
            response = self.client.models.generate_content(
                model=model_name,
                contents=contents,
                config=config_params
            )
            print("DEBUG-RAW-RESPONSE:", response) #to check the error

            return response
        except Exception as e: # added lines inside except
            import traceback
            error_text = traceback.format_exc()

            # Print inside Streamlit so you can SEE it in Colab UI
            import streamlit as st
            st.error("🔥 GEMINI API ERROR")
            st.code(error_text)

            # Also print in logs (just in case)
            print("GEMINI ERROR:", error_text)
            return None  # So Streamlit won't crash immediately

            # raise RuntimeError(f"Error calling Gemini API: {e}")

    def _extract_text(self, response):
        """Tolerant extractor for response text depending on SDK return format."""
        # Many SDKs expose text or a nested structure.
        try:
            # direct attribute
            if hasattr(response, "text") and response.text:
                return response.text
            # try candidates/content (SDK-specific)
            if hasattr(response, "candidates") and response.candidates:
                # candidates may have content or parts
                cand = response.candidates[0]
                if hasattr(cand, "content"):
                    return getattr(cand, "content")
                if hasattr(cand, "message") and hasattr(cand.message, "content"):
                    # content may be list of parts
                    parts = cand.message.content
                    if isinstance(parts, (list, tuple)) and parts:
                        # join parts
                        return " ".join([getattr(p, "text", str(p)) for p in parts])
            # final fallback: string representation
            return str(response)
        except Exception:
            return str(response)

    def get_empathetic_response(self, user_input: str, persona: str, conversation_history: list) -> str:
        """Generates a chat response based on user input, persona, and history."""
        persona_instructions = {
            "peer": "Respond like a supportive, non-professional friend your own age.",
            "mentor": "Respond like a guiding, encouraging, and experienced mentor.",
            "therapist": "Respond like a gentle, non-directive, and empathetic therapist (without giving medical advice)."
        }
        full_system_instruction = BASE_SYSTEM_INSTRUCTION + "\n\n" + persona_instructions.get(persona, persona_instructions['therapist'])
        
        # Format conversation history for Gemini API (SDK expects Content/Part objects)
        gemini_history = []
        for message in conversation_history:
            role = "user" if message["role"] == "user" else "model"
            gemini_history.append(types.Content(role=role, parts=[types.Part.from_text(message["content"])]))
        gemini_history.append(types.Content(role="user", parts=[types.Part.from_text(user_input)]))
        
        response = self._generate_content(
            model_name=MODEL,
            contents=gemini_history,
            system_instruction=full_system_instruction
        )
        text = self._extract_text(response)
        return text

    def generate_cbt_insight(self, thought_record: dict) -> dict:
        prompt = f"""
        Analyze the following thought record and provide structured feedback.
        Thought Record: {json.dumps(thought_record, indent=2)}
        
        Your response MUST be a single JSON object with keys:
        - cognitive_distortions, balanced_thoughts, encouragement
        """
        response = self._generate_content(
            model_name=MODEL,
            contents=prompt,
            system_instruction="You are an expert CBT tool that analyzes text and returns a JSON object for therapy insights.",
            is_json=True
        )
        text = self._extract_text(response)
        return json.loads(text)

    def generate_personalized_journal_prompt(self, mood_context: dict, recent_themes: list) -> dict:
        prompt = f"""
        Based on the user's recent data, create one highly relevant journal prompt and 2-3 follow-up questions.
        Mood Context: {json.dumps(mood_context, indent=2)}
        Recent Journal Themes: {recent_themes}
        Return a JSON object with 'prompt' and 'follow_up_questions'.
        """
        response = self._generate_content(
            model_name=MODEL,
            contents=prompt,
            system_instruction="You are a creative, therapeutic AI that generates personalized journal prompts in JSON format.",
            is_json=True
        )
        text = self._extract_text(response)
        return json.loads(text)

    def analyze_text_for_crisis(self, user_input: str) -> dict:
        prompt = f"Analyze the following user input and determine the risk level (LOW, MODERATE, HIGH, SEVERE) and relevant keywords. User Input: {user_input}"
        response = self._generate_content(
            model_name=MODEL,
            contents=prompt,
            system_instruction=CRISIS_INSTRUCTION,
            is_json=True
        )
        text = self._extract_text(response)
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {"risk_level": "MODERATE", "keywords_detected": ["system_error"], "analysis": "Could not parse AI crisis response."}
