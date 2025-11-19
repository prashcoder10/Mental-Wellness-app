import streamlit as st # type: ignore
import uuid
from datetime import datetime
import os

# Import custom components
from components.chat_interface import render_chat_interface
from components.mood_tracker import render_mood_tracker
from components.journal_prompts import render_journal_prompts
from components.cbt_exercises import render_cbt_exercises
from components.breathing_exercises import render_breathing_exercises
from components.psychoeducation import render_psychoeducation
from utils.data_manager import DataManager
from utils.crisis_detection import CrisisDetector

# Initialize session state for anonymous user
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())
    st.session_state.session_start = datetime.now()

if 'data_manager' not in st.session_state:
    st.session_state.data_manager = DataManager(st.session_state.user_id)

if 'crisis_detector' not in st.session_state:
    st.session_state.crisis_detector = CrisisDetector()

# Set page configuration
st.set_page_config(
    page_title="Youth Mental Wellness Companion",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title and description
st.title("🌱 Youth Mental Wellness Companion")
st.markdown("""
*A safe, anonymous space for mental wellness support and self-care tools.*

**Important Notice:** This chatbot is designed to provide support and self-help tools. 
It is not a replacement for professional mental health care. If you're experiencing a mental health crisis, 
please contact emergency services or call 988 (Suicide & Crisis Lifeline).
""")

# Sidebar navigation
st.sidebar.title("🛠️ Wellness Tools")
st.sidebar.markdown("---")

# Privacy notice in sidebar
st.sidebar.info("""
🔒 **Complete Privacy**
- No personal information required
- Anonymous sessions only
- Data encrypted and secure
- Option to delete all data anytime
""")

# Navigation options
page = st.sidebar.selectbox(
    "Choose a wellness tool:",
    [
        "💬 Chat Support",
        "📊 Mood Tracker", 
        "📝 Guided Journaling",
        "🧠 CBT Exercises",
        "🫁 Breathing & Mindfulness",
        "📚 Learn About Mental Health",
        "⚙️ Privacy Settings"
    ]
)

# Crisis resources always visible
st.sidebar.markdown("---")
st.sidebar.error("""
🚨 **Crisis Resources**
- **Emergency**: Call 911
- **Crisis Text Line**: Text HOME to 741741
- **Suicide Prevention**: Call 988
- **Crisis Chat**: [suicidepreventionlifeline.org](https://suicidepreventionlifeline.org)
""")

# Data management options
st.sidebar.markdown("---")
if st.sidebar.button("🗑️ Delete All My Data"):
    if st.sidebar.button("⚠️ Confirm Delete", type="primary"):
        st.session_state.data_manager.delete_all_data()
        st.sidebar.success("All data deleted successfully")
        st.rerun()

# Main content area based on selected page
if page == "💬 Chat Support":
    render_chat_interface()
elif page == "📊 Mood Tracker":
    render_mood_tracker()
elif page == "📝 Guided Journaling":
    render_journal_prompts()
elif page == "🧠 CBT Exercises":
    render_cbt_exercises()
elif page == "🫁 Breathing & Mindfulness":
    render_breathing_exercises()
elif page == "📚 Learn About Mental Health":
    render_psychoeducation()
elif page == "⚙️ Privacy Settings":
    st.header("🔒 Privacy & Data Settings")
    
    st.subheader("Your Anonymous Session")
    st.info(f"Session ID: {st.session_state.user_id[:8]}... (shortened for privacy)")
    st.info(f"Session started: {st.session_state.session_start.strftime('%Y-%m-%d %H:%M')}")
    
    st.subheader("Data Management")
    st.write("All your data is stored securely and anonymously. You can:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📊 View Data Summary"):
            data_summary = st.session_state.data_manager.get_data_summary()
            st.json(data_summary)
    
    with col2:
        if st.button("💾 Export My Data"):
            export_data = st.session_state.data_manager.export_user_data()
            st.download_button(
                label="Download Data",
                data=export_data,
                file_name=f"wellness_data_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )
    
    st.subheader("Privacy Information")
    st.markdown("""
    **How we protect your privacy:**
    - ✅ No personal information collected
    - ✅ Anonymous session IDs only
    - ✅ Data encrypted at rest
    - ✅ No tracking across sessions
    - ✅ Complete data deletion available
    - ✅ No data sharing with third parties
    
    **Data we collect:**
    - Mood ratings and journal entries (if you choose to save them)
    - Chat messages for providing better support
    - Usage patterns to improve the service
    
    **Data we DON'T collect:**
    - Name, email, or any personal identifiers
    - Location data
    - Device information beyond basic browser data
    - Social media profiles or contacts
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.8em;'>
💙 Remember: You're not alone. Taking care of your mental health is a sign of strength.
</div>
""", unsafe_allow_html=True)
