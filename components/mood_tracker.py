import streamlit as st # type: ignore
import plotly.graph_objects as go # type: ignore
import plotly.express as px # type: ignore
from datetime import datetime, timedelta
import pandas as pd # type: ignore

def render_mood_tracker():
    """Render comprehensive mood tracking interface"""
    
    st.header("📊 Mood Tracker")
    st.markdown("Track your emotions and identify patterns to better understand your mental wellness journey.")
    
    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs(["📝 Log Mood", "📈 View Trends", "🔍 Insights"])
    
    with tab1:
        render_mood_entry()
    
    with tab2:
        render_mood_trends()
    
    with tab3:
        render_mood_insights()

def render_mood_entry():
    """Render mood entry form"""
    
    st.subheader("How are you feeling right now?")
    
    # Overall mood rating
    overall_mood = st.slider(
        "Overall mood (1 = Very Low, 10 = Very High)",
        min_value=1,
        max_value=10,
        value=5,
        help="Rate your general mood right now"
    )
    
    # Emotion selection
    st.subheader("What emotions are you experiencing?")
    
    emotions_options = {
        "😊 Happy": "happy",
        "😢 Sad": "sad", 
        "😰 Anxious": "anxious",
        "😡 Angry": "angry",
        "😴 Tired": "tired",
        "🤗 Grateful": "grateful",
        "😕 Frustrated": "frustrated",
        "😌 Calm": "calm",
        "😔 Lonely": "lonely",
        "💪 Motivated": "motivated",
        "😖 Overwhelmed": "overwhelmed",
        "😐 Neutral": "neutral"
    }
    
    selected_emotions = st.multiselect(
        "Select all that apply:",
        options=list(emotions_options.keys()),
        help="You can select multiple emotions"
    )
    
    # Intensity rating
    intensity = st.slider(
        "How intense are these feelings? (1 = Mild, 10 = Very Intense)",
        min_value=1,
        max_value=10,
        value=5
    )
    
    # Triggers/context
    st.subheader("What might have influenced your mood?")
    
    trigger_options = [
        "School/Work stress",
        "Relationship issues", 
        "Family situations",
        "Health concerns",
        "Financial worries",
        "Social situations",
        "Sleep issues",
        "Weather/environment",
        "Social media",
        "Physical activity",
        "Nothing specific",
        "Other"
    ]
    
    triggers = st.multiselect(
        "Potential triggers or influences:",
        options=trigger_options
    )
    
    # Additional notes
    notes = st.text_area(
        "Additional thoughts or notes (optional):",
        placeholder="Anything else you'd like to note about your mood today...",
        height=100
    )
    
    # Save mood entry
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("💾 Save Entry", type="primary"):
            mood_data = {
                "overall_mood": overall_mood,
                "emotions": [emotions_options[emotion] for emotion in selected_emotions],
                "intensity": intensity,
                "triggers": triggers,
                "notes": notes
            }
            
            st.session_state.data_manager.save_mood_entry(mood_data)
            st.success("Mood entry saved! 📊")
            st.balloons()
    
    # Quick mood check-ins
    st.markdown("---")
    st.subheader("⚡ Quick Check-ins")
    st.markdown("For faster tracking, use these preset mood combinations:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("😔 Having a tough day"):
            quick_mood = {
                "overall_mood": 3,
                "emotions": ["sad", "overwhelmed"],
                "intensity": 6,
                "triggers": ["Other"],
                "notes": "Quick check-in: Having a tough day"
            }
            st.session_state.data_manager.save_mood_entry(quick_mood)
            st.success("Quick mood logged!")
    
    with col2:
        if st.button("😐 Feeling okay"):
            quick_mood = {
                "overall_mood": 6,
                "emotions": ["neutral", "calm"],
                "intensity": 4,
                "triggers": ["Nothing specific"],
                "notes": "Quick check-in: Feeling okay"
            }
            st.session_state.data_manager.save_mood_entry(quick_mood)
            st.success("Quick mood logged!")
    
    with col3:
        if st.button("😊 Having a good day"):
            quick_mood = {
                "overall_mood": 8,
                "emotions": ["happy", "motivated"],
                "intensity": 5,
                "triggers": ["Nothing specific"],
                "notes": "Quick check-in: Having a good day"
            }
            st.session_state.data_manager.save_mood_entry(quick_mood)
            st.success("Quick mood logged!")

def render_mood_trends():
    """Render mood trends and visualizations"""
    
    if not st.session_state.mood_entries:
        st.info("📈 Start logging your moods to see trends and patterns here!")
        return
    
    st.subheader("📈 Your Mood Trends")
    
    # Get mood trends data
    trends = st.session_state.data_manager.get_mood_trends()
    
    if not trends["dates"]:
        st.info("No mood data available yet. Start tracking to see your trends!")
        return
    
    # Create mood line chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=trends["dates"],
        y=trends["moods"],
        mode='lines+markers',
        name='Daily Mood',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=8)
    ))
    
    # Add average line
    fig.add_hline(
        y=trends["average"],
        line_dash="dash",
        line_color="red",
        annotation_text=f"Average: {trends['average']}"
    )
    
    fig.update_layout(
        title="Mood Over Time",
        xaxis_title="Date",
        yaxis_title="Mood Rating (1-10)",
        yaxis=dict(range=[1, 10]),
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Recent mood summary
    recent_moods = st.session_state.data_manager.get_recent_mood_data(7)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if recent_moods:
            recent_avg = sum(entry["overall_mood"] for entry in recent_moods) / len(recent_moods)
            st.metric("7-Day Average", f"{recent_avg:.1f}", f"{recent_avg - trends['average']:.1f}")
        else:
            st.metric("7-Day Average", "No data")
    
    with col2:
        if trends["moods"]:
            st.metric("Highest Mood", max(trends["moods"]))
        else:
            st.metric("Highest Mood", "No data")
    
    with col3:
        if trends["moods"]:
            st.metric("Lowest Mood", min(trends["moods"]))
        else:
            st.metric("Lowest Mood", "No data")
    
    # Emotion frequency chart
    st.subheader("🎭 Most Common Emotions")
    
    emotion_counts = {}
    for entry in st.session_state.mood_entries:
        for emotion in entry.get("emotions", []):
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
    
    if emotion_counts:
        emotions_data = list(emotion_counts.items())
        if emotions_data:
            emotions_df = pd.DataFrame(emotions_data, columns=["Emotion", "Count"]).sort_values("Count", ascending=True)
            
            fig = px.bar(
                emotions_df,
                x="Count",
                y="Emotion",
                orientation='h',
                title="Emotion Frequency"
            )
            
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    # Trigger analysis
    st.subheader("🔍 Common Triggers")
    
    trigger_counts = {}
    for entry in st.session_state.mood_entries:
        for trigger in entry.get("triggers", []):
            trigger_counts[trigger] = trigger_counts.get(trigger, 0) + 1
    
    if trigger_counts:
        # Show top 5 triggers
        sorted_triggers = sorted(trigger_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        
        for i, (trigger, count) in enumerate(sorted_triggers, 1):
            st.write(f"{i}. **{trigger}**: {count} times")

def render_mood_insights():
    """Render AI-generated insights about mood patterns"""
    
    if len(st.session_state.mood_entries) < 3:
        st.info("🔍 Log at least 3 mood entries to get personalized insights!")
        return
    
    st.subheader("🧠 Your Mood Insights")
    
    # Calculate some basic insights
    recent_entries = st.session_state.mood_entries[-10:]  # Last 10 entries
    
    # Mood stability
    mood_values = [entry["overall_mood"] for entry in recent_entries]
    mood_range = max(mood_values) - min(mood_values)
    
    if mood_range <= 2:
        stability = "Very stable"
        stability_color = "🟢"
    elif mood_range <= 4:
        stability = "Moderately stable"
        stability_color = "🟡"
    else:
        stability = "Variable"
        stability_color = "🟠"
    
    st.write(f"**Mood Stability:** {stability_color} {stability}")
    
    # Most common emotions
    all_emotions = []
    for entry in recent_entries:
        all_emotions.extend(entry.get("emotions", []))
    
    if all_emotions:
        emotion_counts = {}
        for emotion in all_emotions:
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
        
        top_emotion = max(emotion_counts.items(), key=lambda x: x[1])
        st.write(f"**Most frequent emotion:** {top_emotion[0].title()} ({top_emotion[1]} times)")
    
    # Trigger patterns
    all_triggers = []
    for entry in recent_entries:
        all_triggers.extend(entry.get("triggers", []))
    
    if all_triggers:
        trigger_counts = {}
        for trigger in all_triggers:
            trigger_counts[trigger] = trigger_counts.get(trigger, 0) + 1
        
        if trigger_counts:
            top_trigger = max(trigger_counts.items(), key=lambda x: x[1])
            st.write(f"**Most common trigger:** {top_trigger[0]} ({top_trigger[1]} times)")
    
    # Personalized recommendations
    st.subheader("💡 Personalized Recommendations")
    
    avg_mood = sum(mood_values) / len(mood_values)
    
    if avg_mood < 4:
        st.warning("""
        Your recent mood has been on the lower side. Consider:
        - 🧘 Try daily breathing exercises
        - 📝 Use guided journaling to explore your feelings
        - 🚶 Gentle physical activity like walking
        - 🤝 Reach out to someone you trust
        - 🩺 Consider speaking with a mental health professional
        """)
    elif avg_mood < 6:
        st.info("""
        Your mood has been moderate. To boost your wellbeing:
        - 🎯 Set small, achievable daily goals
        - 📚 Try some psychoeducational content
        - 🧠 Practice CBT exercises to challenge negative thoughts
        - 😊 Focus on gratitude and positive experiences
        """)
    else:
        st.success("""
        Your mood has been generally positive! To maintain this:
        - 🎉 Celebrate your progress
        - 📊 Continue regular mood tracking
        - 🔄 Share positive coping strategies with others
        - 🛡️ Build resilience for future challenges
        """)
    
    # Data export option
    st.markdown("---")
    if st.button("📊 Export Mood Data"):
        mood_df = pd.DataFrame(st.session_state.mood_entries)
        csv = mood_df.to_csv(index=False)
        
        st.download_button(
            label="Download Mood Data CSV",
            data=csv,
            file_name=f"mood_data_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
