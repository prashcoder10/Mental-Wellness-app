# components/chat_interface.py

import streamlit as st # type: ignore
from utils.gemini_client import GeminiClient # 🌟 CHANGE: Import GeminiClient
from utils.crisis_detection import CrisisDetector

def render_chat_interface():
    """Render the main chat interface with crisis detection"""
    
    st.header("💬 Chat Support")
    st.markdown("Choose your support style and start a conversation.")
    
    # Initialize components with Gemini client
    if 'gemini_client' not in st.session_state: # 🌟 CHANGE: Client variable name
        st.session_state.gemini_client = GeminiClient() # 🌟 CHANGE: Use GeminiClient
    
    if 'crisis_detector' not in st.session_state:
        st.session_state.crisis_detector = CrisisDetector()
    
    # Persona selection
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("👥 Peer Support"): st.session_state.current_persona = "peer"
    with col2:
        if st.button("🌟 Mentor"): st.session_state.current_persona = "mentor"
    with col3:
        if st.button("🧑‍⚕️ Therapist"): st.session_state.current_persona = "therapist"
    
    if 'current_persona' not in st.session_state:
        st.session_state.current_persona = "therapist"

    # Display current persona
    persona_names = {"peer": "Peer Support", "mentor": "Mentor", "therapist": "Therapist"}
    st.info(f"Current support style: {persona_names[st.session_state.current_persona]}")
    
    # Chat history display
    for message in st.session_state.get('chat_history', []):
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    user_input = st.chat_input("What's on your mind?")
    
    if user_input:
        st.session_state.data_manager.save_chat_message("user", user_input)
        
        # Note: CrisisDetector should also be updated to use the new client if its internal logic relies on it.
        # Assuming CrisisDetector uses st.session_state.gemini_client or a fallback logic for now.
        risk_assessment = st.session_state.crisis_detector.analyze_text_for_crisis(user_input)
        crisis_detected = st.session_state.crisis_detector.trigger_crisis_intervention(risk_assessment)
        
        conversation_history = st.session_state.data_manager.get_conversation_history()
        
        try:
            # 🌟 CHANGE: Use gemini_client and new method
            ai_response = st.session_state.gemini_client.get_empathetic_response(
                user_input, 
                st.session_state.current_persona,
                conversation_history
            )
            
            if crisis_detected:
                follow_up = st.session_state.crisis_detector.get_crisis_follow_up_message(risk_assessment["final_risk_level"])
                ai_response = f"{ai_response}\n\n{follow_up}"
            
            st.session_state.data_manager.save_chat_message("assistant", ai_response)
        except Exception as e:
            st.error(f"Error getting response: {e}")

        st.rerun()