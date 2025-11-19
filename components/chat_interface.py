# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("What's on your mind?")

if user_input:
    # Add user message to UI immediately
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Save to DB also
    st.session_state.data_manager.save_chat_message(
        "user", user_input, persona=st.session_state.current_persona
    )

    # Crisis detection
    risk_assessment = st.session_state.crisis_detector.analyze_text_for_crisis(user_input)
    crisis_detected = st.session_state.crisis_detector.trigger_crisis_intervention(risk_assessment)

    # Show user message immediately
    with st.chat_message("user"):
        st.write(user_input)

    # Generate AI response
    try:
        ai_response = st.session_state.gemini_client.get_empathetic_response(
            user_input,
            st.session_state.current_persona,
            st.session_state.data_manager.get_conversation_history()
        )

        if crisis_detected:
            follow_up = st.session_state.crisis_detector.get_crisis_follow_up_message(
                risk_assessment["final_risk_level"]
            )
            ai_response += "\n\n" + follow_up

    except Exception:
        ai_response = "I'm having trouble responding right now. Please try again."

    # Add bot message to UI immediately
    st.session_state.chat_history.append({"role": "assistant", "content": ai_response})

    # Save to DB
    st.session_state.data_manager.save_chat_message(
        "assistant", ai_response, persona=st.session_state.current_persona
    )

    # Display bot response
    with st.chat_message("assistant"):
        st.write(ai_response)
