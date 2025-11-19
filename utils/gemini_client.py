# utils/gemini_client.py

import os
import json
from google import genai
from google.genai import types

# Define the model to use
MODEL = 'gemini-2.5-flash'

# System Instruction for the main chat (Therapist Persona)
BASE_SYSTEM_INSTRUCTION = """
You are a compassionate, non-judgmental, and supportive mental wellness companion. 
Your primary role is to listen empathetically, validate feelings, and provide evidence-based mental health support, 
such as guided journaling, CBT principles, and breathing exercises.
ALWAYS prioritize user safety. If the user expresses thoughts of self-harm or suicide,
immediately and gently pivot to providing the crisis resources already listed in the prompt.
NEVER provide diagnosis or claim to be a human professional.
Keep responses concise, warm, and focused on the user's emotional state.
"""

# Crisis Handling System Instruction
CRISIS_INSTRUCTION = """
You are a highly sensitive and empathetic crisis detection AI. Analyze the user's message 
for themes related to self-harm, suicidal ideation, severe distress, or abuse.
Your response MUST be a single JSON object.

Example output if severe risk:
{"risk_level": "SEVERE", "keywords_detected": ["kill myself", "end it all"], "analysis": "The user expresses immediate suicidal intent."}

Example output if low risk:
{"risk_level": "LOW", "keywords_detected": ["stressed", "sad"], "analysis": "The user is expressing general sadness and stress."}

Risk Levels are: LOW, MODERATE, HIGH, SEVERE. 
Focus your detection on identifying the presence of immediate danger or clear plans for self-harm.
"""

class GeminiClient:
    def __init__(self):
        """Initializes the Gemini client, picking up the API key from the environment."""
        if "GEMINI_API_KEY" not in os.environ:
            st.error("GEMINI_API_KEY not found. Please set the environment variable.")
            self.client = None
        else:
            self.client = genai.Client()

    def _generate_content(self, model_name: str, contents, system_instruction: str, is_json: bool = False):
        """Helper function to call the Gemini API."""
        if not self.client:
            raise Exception("Gemini client is not initialized. Check GEMINI_API_KEY.")
        
        config_params = {
            "system_instruction": system_instruction,
            "temperature": 0.7 if not is_json else 0.0 # Use low temp for JSON
        }

        if is_json:
            config_params["response_mime_type"] = "application/json"
        
        response = self.client.models.generate_content(
            model=model_name,
            contents=contents,
            config=config_params
        )
        return response

    def get_empathetic_response(self, user_input: str, persona: str, conversation_history: list) -> str:
        """Generates a chat response based on user input, persona, and history."""
        
        persona_instructions = {
            "peer": "Respond like a supportive, non-professional friend your own age.",
            "mentor": "Respond like a guiding, encouraging, and experienced mentor.",
            "therapist": "Respond like a gentle, non-directive, and empathetic therapist (without giving medical advice)."
        }
        
        full_system_instruction = BASE_SYSTEM_INSTRUCTION + "\n\n" + persona_instructions.get(persona, persona_instructions['therapist'])
        
        # Format conversation history for Gemini API
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
        return response.text

    def generate_cbt_insight(self, thought_record: dict) -> dict:
        """Generates AI insights for a thought record."""
        prompt = f"""
        Analyze the following thought record and provide structured feedback.
        Thought Record: {json.dumps(thought_record, indent=2)}
        
        Your response MUST be a single JSON object with the following keys:
        - "cognitive_distortions": A list of potential cognitive distortions (e.g., ["All-or-Nothing Thinking", "Catastrophizing"])
        - "balanced_thoughts": A list of 2-3 alternative, more balanced thoughts
        - "encouragement": A short, empathetic encouraging message.
        """
        response = self._generate_content(
            model_name=MODEL,
            contents=prompt,
            system_instruction="You are an expert CBT tool that analyzes text and returns a JSON object for therapy insights.",
            is_json=True
        )
        return json.loads(response.text)

    def generate_personalized_journal_prompt(self, mood_context: dict, recent_themes: list) -> dict:
        """Generates a personalized journal prompt based on user data."""
        prompt = f"""
        Based on the user's recent data, create one highly relevant journal prompt and 2-3 follow-up questions.
        Mood Context (Recent Average Mood, Common Emotions): {json.dumps(mood_context, indent=2)}
        Recent Journal Themes: {recent_themes}
        
        The prompt should be designed to help the user explore the emotions or patterns identified in the context.
        
        Your response MUST be a single JSON object with the following keys:
        - "prompt": The personalized journal prompt
        - "follow_up_questions": A list of 2-3 specific follow-up questions for deeper reflection.
        """
        response = self._generate_content(
            model_name=MODEL,
            contents=prompt,
            system_instruction="You are a creative, therapeutic AI that generates personalized journal prompts in JSON format.",
            is_json=True
        )
        return json.loads(response.text)

    def analyze_text_for_crisis(self, user_input: str) -> dict:
        """Analyzes text for crisis indicators (Note: This is a placeholder for a dedicated model)."""
        prompt = f"Analyze the following user input and determine the risk level (LOW, MODERATE, HIGH, SEVERE) and relevant keywords. User Input: {user_input}"
        
        response = self._generate_content(
            model_name=MODEL,
            contents=prompt,
            system_instruction=CRISIS_INSTRUCTION,
            is_json=True
        )
        try:
            return json.loads(response.text)
        except json.JSONDecodeError:
            # Fallback if the model doesn't return perfect JSON
            return {"risk_level": "MODERATE", "keywords_detected": ["system_error"], "analysis": "Could not parse AI crisis response."}