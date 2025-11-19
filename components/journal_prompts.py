import streamlit as st # type: ignore
from datetime import datetime
from utils.gemini_client import GeminiClient  # 🌟 CHANGE: Import GeminiClient
from data.journal_prompts import JOURNAL_PROMPTS, CBT_PROMPTS

def render_journal_prompts():
    """Render guided journaling interface with CBT-based prompts"""
    
    st.header("📝 Guided Journaling")
    st.markdown("Explore your thoughts and feelings through guided reflection. Journaling can help you process emotions and gain insights.")
    
    # Initialize Gemini client
    if 'gemini_client' not in st.session_state: # 🌟 CHANGE: Client variable name
        st.session_state.gemini_client = GeminiClient() # 🌟 CHANGE: Use GeminiClient
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["✍️ New Entry", "📚 Your Entries", "🤖 AI-Personalized"])
    
    with tab1:
        render_new_journal_entry()
    
    with tab2:
        render_journal_history()
    
    with tab3:
        render_ai_personalized_prompts()

# The rest of render_new_journal_entry and render_journal_history remains the same.

def render_new_journal_entry():
    """Render interface for creating new journal entry"""
    
    st.subheader("Choose Your Journaling Focus")
    
    # Focus area selection
    focus_areas = {
        "🎭 Emotional Awareness": "emotional_awareness",
        "🧠 Thought Patterns": "thought_patterns", 
        "🙏 Gratitude & Positivity": "gratitude",
        "💪 Coping & Resilience": "coping_skills",
        "🎯 Goals & Growth": "goals",
        "👥 Relationships": "relationships",
        "🌅 Daily Reflection": "daily_reflection"
    }
    
    selected_focus = st.selectbox(
        "What would you like to focus on today?",
        options=list(focus_areas.keys())
    )
    
    focus_key = focus_areas[selected_focus]
    
    # Get prompts for selected focus area
    available_prompts = JOURNAL_PROMPTS.get(focus_key, [])
    cbt_prompts = CBT_PROMPTS.get(focus_key, [])
    
    # Combine and select prompt
    all_prompts = available_prompts + cbt_prompts
    
    if all_prompts:
        col1, col2 = st.columns([3, 1])
        with col1:
            selected_prompt = st.selectbox(
                "Choose a prompt or get a random one:",
                options=["🎲 Surprise me with a random prompt"] + all_prompts
            )
        with col2:
            if st.button("🔄 New Random Prompt"):
                import random
                selected_prompt = random.choice(all_prompts)
                st.rerun()
    else:
        selected_prompt = "What's on your mind today? Write about anything that feels important to you right now."
    
    # Display the prompt
    if selected_prompt.startswith("🎲"):
        import random
        actual_prompt = random.choice(all_prompts) if all_prompts else "What are you grateful for today?"
    else:
        actual_prompt = selected_prompt
    
    st.markdown("### 💭 Your Prompt")
    st.info(f"**{actual_prompt}**")
    
    # Pre-writing mood check
    st.subheader("How are you feeling before writing?")
    col1, col2 = st.columns(2)
    with col1:
        mood_before = st.slider("Mood before writing (1-10)", 1, 10, 5, key="mood_before")
    with col2:
        emotional_state = st.selectbox(
            "Primary emotion right now:",
            ["Calm", "Anxious", "Sad", "Happy", "Frustrated", "Confused", "Motivated", "Tired", "Other"]
        )
    
    # Writing area
    st.subheader("✍️ Your Reflection")
    journal_content = st.text_area(
        "Write your thoughts here...",
        placeholder="Take your time and write whatever comes to mind...",
        height=300,
        key="journal_content"
    )
    
    insights = ""
    if journal_content:
        st.subheader("🤔 Follow-up Reflection")
        follow_up_prompts = [
            "What emotions came up while writing this?",
            "What insights or patterns do you notice?",
            "How might you apply this reflection to your daily life?",
        ]
        insights = st.text_area(
            "Optional: Reflect on these questions:",
            placeholder="\n".join(f"• {prompt}" for prompt in follow_up_prompts),
            height=150,
            key="insights"
        )
    
    st.subheader("How are you feeling after writing?")
    mood_after = st.slider("Mood after writing (1-10)", 1, 10, mood_before, key="mood_after")
    
    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        if st.button("💾 Save Entry", type="primary"):
            if journal_content.strip():
                entry_data = {
                    "prompt": actual_prompt,
                    "content": journal_content,
                    "focus_area": focus_key,
                    "mood_before": mood_before,
                    "mood_after": mood_after,
                    "emotional_state": emotional_state,
                    "insights": insights
                }
                st.session_state.data_manager.save_journal_entry(entry_data)
                st.success("Journal entry saved! 📖")
                mood_change = mood_after - mood_before
                if mood_change > 1:
                    st.balloons()
                    st.success(f"Great! Your mood improved by {mood_change} points! 📈")
                elif mood_change < -1:
                    st.info("Writing can bring up tough emotions. That's part of the process. 💙")
            else:
                st.warning("Please write something before saving.")
    with col2:
        if st.button("🗑️ Clear"):
            st.rerun()

def render_journal_history():
    """Display previous journal entries"""
    if not st.session_state.get('journal_entries'):
        st.info("📝 Your journal entries will appear here once you start writing!")
        return
    
    st.subheader("📚 Your Journal History")
    sorted_entries = sorted(st.session_state.journal_entries, key=lambda x: x["timestamp"], reverse=True)
    
    for entry in sorted_entries:
        with st.expander(f"📝 {datetime.fromisoformat(entry['timestamp']).strftime('%B %d, %Y')} - {entry.get('focus_area', 'general').replace('_', ' ').title()}"):
            st.markdown(f"**Prompt:** {entry.get('prompt', 'Free writing')}")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Mood Before", entry.get('mood_before', 0))
            with col2:
                mood_change = entry.get('mood_after', 0) - entry.get('mood_before', 0)
                st.metric("Mood After", entry.get('mood_after', 0), f"{mood_change:+d}")
            with col3:
                st.write(f"**Emotion:** {entry.get('emotional_state', 'N/A')}")
            st.markdown("**Your Writing:**")
            st.write(entry.get('content', ''))
            if entry.get('insights'):
                st.markdown("**Your Insights:**")
                st.write(entry.get('insights'))

def render_ai_personalized_prompts():
    """Generate AI-personalized journal prompts based on user data"""
    st.subheader("🤖 AI-Personalized Prompts")
    st.markdown("Get journal prompts tailored to your recent mood patterns and entries.")
    
    if len(st.session_state.get('mood_entries', [])) < 2 and len(st.session_state.get('journal_entries', [])) < 1:
        st.info("🔄 **Not enough data yet!** To get personalized prompts, log a few moods or write a journal entry.")
        return
    
    if st.button("✨ Generate Personalized Prompt", type="primary"):
        with st.spinner("Creating your personalized prompt..."):
            recent_moods = st.session_state.data_manager.get_recent_mood_data(7)
            recent_themes = st.session_state.data_manager.get_journal_themes()
            mood_context = {
                "recent_average": sum(m["overall_mood"] for m in recent_moods) / len(recent_moods) if recent_moods else 5,
                "common_emotions": [m.get("emotions", []) for m in recent_moods],
            }
            try:
                # 🌟 CHANGE: Use gemini_client and new method
                personalized_prompt = st.session_state.gemini_client.generate_personalized_journal_prompt(
                    mood_context, 
                    recent_themes[:3]
                )
                st.success("✨ Your Personalized Prompt")
                st.info(f"**{personalized_prompt['prompt']}**")
                if personalized_prompt.get('follow_up_questions'):
                    st.markdown("**Consider these follow-up questions:**")
                    for i, question in enumerate(personalized_prompt['follow_up_questions'], 1):
                        st.write(f"{i}. {question}")
            except Exception as e:
                st.error("Unable to generate personalized prompt right now. Try one of the pre-written prompts instead!")