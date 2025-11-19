# # components/chat_interface.py

# import streamlit as st # type: ignore
# from utils.gemini_client import GeminiClient
# from utils.crisis_detection import CrisisDetector
# from utils.data_manager import DataManager
# import uuid

# def render_chat_interface():
#     st.header("💬 Chat Support")
#     st.markdown("Choose your support style and start a conversation.")
    
#     # create session_start if missing
#     if 'session_start' not in st.session_state:
#         st.session_state.session_start = __import__('datetime').datetime.now().isoformat()

#     # Initialize data_manager if not present (generate anonymous id)
#     if 'data_manager' not in st.session_state:
#         st.session_state.data_manager = DataManager(user_id=str(uuid.uuid4()))
    
#     # Initialize Gemini client (show friendly message if missing)
#     if 'gemini_client' not in st.session_state:
#         try:
#             st.session_state.gemini_client = GeminiClient()
#         except Exception as e:
#             st.error(f"Gemini client init error: {e}")
#             st.session_state.gemini_client = None
    
#     # Initialize crisis detector (will reuse session gemini_client if present)
#     if 'crisis_detector' not in st.session_state:
#         st.session_state.crisis_detector = CrisisDetector()
    
#     # Persona selection
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         if st.button("👥 Peer Support"):
#             st.session_state.current_persona = "peer"
#     with col2:
#         if st.button("🌟 Mentor"):
#             st.session_state.current_persona = "mentor"
#     with col3:
#         if st.button("🧑‍⚕️ Therapist"):
#             st.session_state.current_persona = "therapist"
    
#     if 'current_persona' not in st.session_state:
#         st.session_state.current_persona = "therapist"

#     persona_names = {"peer": "Peer Support", "mentor": "Mentor", "therapist": "Therapist"}
#     st.info(f"Current support style: {persona_names.get(st.session_state.current_persona, 'Therapist')}")
    
#     # Chat history display
#     for message in st.session_state.get('chat_history', []):
#         with st.chat_message(message["role"]):
#             st.write(message["content"])

#     # Chat input
#     user_input = st.chat_input("What's on your mind?")
#     print("DEBUG-SENDING-TO-GEMINI:", user_input) ##added lines

#     if user_input:
#         # Save user message
#         try:
#             st.session_state.data_manager.save_chat_message("user", user_input, persona=st.session_state.current_persona)
#         except Exception as e:
#             st.error(f"Error saving user message: {e}")
        
#         # Crisis detection
#         risk_assessment = st.session_state.crisis_detector.analyze_text_for_crisis(user_input)
#         crisis_detected = st.session_state.crisis_detector.trigger_crisis_intervention(risk_assessment)
        
#         conversation_history = st.session_state.data_manager.get_conversation_history()
        
#         try:
#             if st.session_state.gemini_client is None:
#                 raise RuntimeError("Gemini client unavailable. Check API key.")
            
#             ai_response = st.session_state.gemini_client.get_empathetic_response(
#                 user_input, 
#                 st.session_state.current_persona,
#                 conversation_history
#             )
#             print("DEBUG-GEMINI-RESPONSE:", ai_response) ##added lines

#             if crisis_detected:
#                 follow_up = st.session_state.crisis_detector.get_crisis_follow_up_message(risk_assessment["final_risk_level"])
#                 ai_response = f"{ai_response}\n\n{follow_up}"
            
#             st.session_state.data_manager.save_chat_message("assistant", ai_response, persona=st.session_state.current_persona)
#         except Exception as e:
#             st.error(f"Error getting assistant response: {e}")
#             # Save fallback assistant message so user gets something instead of nothing
#             fallback = "Sorry — I'm having trouble generating a response right now. Please try again in a moment."
#             try:
#                 st.session_state.data_manager.save_chat_message("assistant", fallback, persona=st.session_state.current_persona)
#             except Exception:
#                 pass

#         # Do not call st.rerun() immediately — let the UI update normally.


# components/chat_interface.py

import streamlit as st
from utils.gemini_client import GeminiClient
from utils.crisis_detection import CrisisDetector
from utils.data_manager import DataManager
import uuid


def render_chat_interface():
    st.header("💬 Chat Support")
    st.markdown("Choose your support style and start a conversation.")

    # ---------------------
    # INITIALIZATION
    # ---------------------
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "last_processed_input" not in st.session_state:
        st.session_state.last_processed_input = None

    if 'session_start' not in st.session_state:
        st.session_state.session_start = __import__('datetime').datetime.now().isoformat()

    if 'data_manager' not in st.session_state:
        st.session_state.data_manager = DataManager(user_id=str(uuid.uuid4()))

    if 'gemini_client' not in st.session_state:
        try:
            st.session_state.gemini_client = GeminiClient()
        except:
            st.session_state.gemini_client = None

    if 'crisis_detector' not in st.session_state:
        st.session_state.crisis_detector = CrisisDetector()

    if 'current_persona' not in st.session_state:
        st.session_state.current_persona = "therapist"

    # ---------------------
    # FIX 1: Use radio instead of button
    # ---------------------
    persona = st.radio(
        "Support Style",
        ["peer", "mentor", "therapist"],
        index=["peer", "mentor", "therapist"].index(st.session_state.current_persona),
        horizontal=True,
        key="persona_selector"
    )
    st.session_state.current_persona = persona

    persona_display = {
        "peer": "Peer Support",
        "mentor": "Mentor",
        "therapist": "Therapist"
    }
    st.info(f"Current support style: {persona_display[persona]}")

    # ---------------------
    # DISPLAY CHAT HISTORY
    # ---------------------
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # ---------------------
    # USER INPUT
    # ---------------------
    user_input = st.chat_input("What's on your mind?")

    # Only process if new input (FIX 2)
    if user_input and user_input != st.session_state.last_processed_input:

        st.session_state.last_processed_input = user_input

        # Add to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Save user message
        st.session_state.data_manager.save_chat_message(
            "user", user_input, persona=persona
        )

        # Crisis detection
        risk = st.session_state.crisis_detector.analyze_text_for_crisis(user_input)
        st.session_state.crisis_detector.trigger_crisis_intervention(risk)

        # Get conversation history
        convo = st.session_state.data_manager.get_conversation_history()

        # Get AI response
        try:
            ai = st.session_state.gemini_client.get_empathetic_response(
                user_input, persona, convo
            )
        except:
            ai = "Sorry, I'm having trouble generating a response right now."

        # Add crisis follow-up if needed
        if risk["immediate_crisis"] or risk["requires_intervention"]:
            follow = st.session_state.crisis_detector.get_crisis_follow_up_message(
                risk["final_risk_level"]
            )
            ai = f"{ai}\n\n{follow}"

        # Save AI message
        st.session_state.chat_history.append({"role": "assistant", "content": ai})
        st.session_state.data_manager.save_chat_message("assistant", ai, persona=persona)

        # Update UI
        st.rerun()
