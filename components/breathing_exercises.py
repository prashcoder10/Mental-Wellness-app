import streamlit as st # type: ignore
import time
from datetime import datetime
import plotly.graph_objects as go # type: ignore

def render_breathing_exercises():
    """Render breathing exercises and mindfulness activities"""
    
    st.header("🫁 Breathing & Mindfulness")
    st.markdown("Practice breathing techniques and mindfulness exercises to reduce stress and anxiety.")
    
    # Create tabs for different activities
    tab1, tab2, tab3, tab4 = st.tabs(["🫁 Guided Breathing", "🧘 Mindfulness", "🌱 Quick Calming", "📊 Your Practice"])
    
    with tab1:
        render_guided_breathing()
    
    with tab2:
        render_mindfulness_exercises()
    
    with tab3:
        render_quick_calming()
    
    with tab4:
        render_practice_tracking()

def render_guided_breathing():
    """Render guided breathing exercises"""
    
    st.subheader("🫁 Guided Breathing Exercises")
    st.markdown("Choose a breathing technique to practice. These exercises can help reduce anxiety and promote relaxation.")
    
    # Breathing technique selection
    technique = st.selectbox(
        "Choose a breathing technique:",
        [
            "4-7-8 Breathing (Relaxation)",
            "Box Breathing (Focus & Calm)", 
            "Triangle Breathing (Anxiety Relief)",
            "Deep Belly Breathing (Stress Relief)",
            "Coherent Breathing (Balance)"
        ]
    )
    
    # Technique descriptions
    technique_info = {
        "4-7-8 Breathing (Relaxation)": {
            "description": "Inhale for 4, hold for 7, exhale for 8. Great for falling asleep and deep relaxation.",
            "pattern": [4, 7, 8],
            "phases": ["Inhale", "Hold", "Exhale"],
            "benefits": "Promotes relaxation, reduces anxiety, helps with sleep"
        },
        "Box Breathing (Focus & Calm)": {
            "description": "Inhale for 4, hold for 4, exhale for 4, hold for 4. Used by Navy SEALs for focus.",
            "pattern": [4, 4, 4, 4],
            "phases": ["Inhale", "Hold", "Exhale", "Hold"],
            "benefits": "Improves focus, reduces stress, enhances performance"
        },
        "Triangle Breathing (Anxiety Relief)": {
            "description": "Inhale for 4, hold for 4, exhale for 4. Simple and effective for anxiety.",
            "pattern": [4, 4, 4],
            "phases": ["Inhale", "Hold", "Exhale"],
            "benefits": "Quick anxiety relief, easy to remember, discreet"
        },
        "Deep Belly Breathing (Stress Relief)": {
            "description": "Slow, deep breathing into your belly for 6 seconds in, 6 seconds out.",
            "pattern": [6, 6],
            "phases": ["Inhale", "Exhale"],
            "benefits": "Activates relaxation response, reduces stress hormones"
        },
        "Coherent Breathing (Balance)": {
            "description": "Breathe at 5 seconds in, 5 seconds out for balance and coherence.",
            "pattern": [5, 5],
            "phases": ["Inhale", "Exhale"],
            "benefits": "Balances nervous system, improves heart rate variability"
        }
    }
    
    info = technique_info[technique]
    
    # Display technique info
    st.info(f"**{technique}**\n\n{info['description']}\n\n**Benefits:** {info['benefits']}")
    
    # Exercise settings
    col1, col2 = st.columns(2)
    
    with col1:
        duration = st.selectbox(
            "Exercise duration:",
            ["1 minute", "2 minutes", "5 minutes", "10 minutes"]
        )
    
    with col2:
        show_visual = st.checkbox("Show breathing guide", value=True)
    
    # Calculate cycles needed
    duration_map = {"1 minute": 60, "2 minutes": 120, "5 minutes": 300, "10 minutes": 600}
    total_seconds = duration_map[duration]
    cycle_time = sum(info['pattern'])
    total_cycles = total_seconds // cycle_time
    
    st.write(f"This will be approximately **{total_cycles} breathing cycles** over **{duration}**.")
    
    # Start breathing exercise
    if st.button("🫁 Start Breathing Exercise", type="primary"):
        
        # Initialize session tracking
        if 'breathing_sessions' not in st.session_state:
            st.session_state.breathing_sessions = []
        
        # Create containers for the exercise
        instruction_container = st.empty()
        progress_container = st.empty()
        visual_container = st.empty() if show_visual else None
        
        try:
            # Run the breathing exercise
            run_breathing_exercise(
                info['pattern'], 
                info['phases'], 
                total_cycles,
                instruction_container,
                progress_container,
                visual_container
            )
            
            # Record the session
            session_data = {
                "timestamp": datetime.now().isoformat(),
                "technique": technique,
                "duration": duration,
                "cycles_completed": total_cycles
            }
            st.session_state.breathing_sessions.append(session_data)
            
            st.success(f"🎉 Great job! You completed {total_cycles} cycles of {technique}!")
            st.balloons()
            
            # Post-exercise check-in
            st.subheader("How do you feel now?")
            col1, col2 = st.columns(2)
            
            with col1:
                relaxation_level = st.slider(
                    "Relaxation level (1-10):",
                    min_value=1,
                    max_value=10,
                    value=7,
                    key="post_breathing_relaxation"
                )
            
            with col2:
                anxiety_level = st.slider(
                    "Anxiety level (1-10):",
                    min_value=1,
                    max_value=10,
                    value=3,
                    key="post_breathing_anxiety"
                )
            
            if st.button("💾 Save Session"):
                session_data["relaxation_after"] = relaxation_level
                session_data["anxiety_after"] = anxiety_level
                st.session_state.breathing_sessions[-1] = session_data
                st.success("Session saved!")
            
        except Exception as e:
            st.error("Exercise was interrupted. That's okay - even a short practice is beneficial!")

def run_breathing_exercise(pattern, phases, total_cycles, instruction_container, progress_container, visual_container):
    """Run the actual breathing exercise with real-time guidance"""
    
    for cycle in range(total_cycles):
        for phase_idx, (duration, phase) in enumerate(zip(pattern, phases)):
            
            # Update instruction
            instruction_container.markdown(f"### {phase} for {duration} seconds")
            
            # Update progress
            overall_progress = (cycle * len(pattern) + phase_idx) / (total_cycles * len(pattern))
            progress_container.progress(overall_progress)
            
            # Visual breathing guide
            if visual_container:
                if phase.lower() == "inhale":
                    create_breathing_visual(visual_container, "expand", duration)
                elif phase.lower() == "exhale":
                    create_breathing_visual(visual_container, "contract", duration)
                else:  # hold
                    create_breathing_visual(visual_container, "hold", duration)
            
            # Count down the phase
            for second in range(duration, 0, -1):
                time.sleep(1)
                if visual_container is None:
                    instruction_container.markdown(f"### {phase} for {second} seconds")
    
    # Clear containers
    instruction_container.empty()
    progress_container.empty()
    if visual_container:
        visual_container.empty()

def create_breathing_visual(container, action, duration):
    """Create visual breathing guide"""
    
    if action == "expand":
        # Growing circle for inhale
        fig = go.Figure()
        fig.add_shape(
            type="circle",
            x0=-1, y0=-1, x1=1, y1=1,
            fillcolor="lightblue",
            line_color="blue",
            opacity=0.7
        )
        fig.update_layout(
            xaxis=dict(range=[-2, 2], showgrid=False, showticklabels=False),
            yaxis=dict(range=[-2, 2], showgrid=False, showticklabels=False),
            title="Breathe In",
            height=300,
            showlegend=False
        )
        
    elif action == "contract":
        # Shrinking circle for exhale
        fig = go.Figure()
        fig.add_shape(
            type="circle",
            x0=-0.5, y0=-0.5, x1=0.5, y1=0.5,
            fillcolor="lightcoral",
            line_color="red",
            opacity=0.7
        )
        fig.update_layout(
            xaxis=dict(range=[-2, 2], showgrid=False, showticklabels=False),
            yaxis=dict(range=[-2, 2], showgrid=False, showticklabels=False),
            title="Breathe Out",
            height=300,
            showlegend=False
        )
        
    else:  # hold
        # Static circle for hold
        fig = go.Figure()
        fig.add_shape(
            type="circle",
            x0=-0.75, y0=-0.75, x1=0.75, y1=0.75,
            fillcolor="lightgreen",
            line_color="green",
            opacity=0.7
        )
        fig.update_layout(
            xaxis=dict(range=[-2, 2], showgrid=False, showticklabels=False),
            yaxis=dict(range=[-2, 2], showgrid=False, showticklabels=False),
            title="Hold",
            height=300,
            showlegend=False
        )
    
    container.plotly_chart(fig, use_container_width=True)

def render_mindfulness_exercises():
    """Render mindfulness and grounding exercises"""
    
    st.subheader("🧘 Mindfulness Exercises")
    st.markdown("Practice mindfulness techniques to stay present and reduce anxiety.")
    
    # Exercise selection
    exercise_type = st.selectbox(
        "Choose a mindfulness exercise:",
        [
            "5-4-3-2-1 Grounding",
            "Body Scan Meditation",
            "Mindful Observation"
        ]
    )
    
    if exercise_type == "5-4-3-2-1 Grounding":
        st.markdown("""
        ### 5-4-3-2-1 Grounding Technique
        
        This exercise helps ground you in the present moment using your five senses.
        
        **Instructions:**
        """)
        
        if st.button("🔍 Start 5-4-3-2-1 Exercise"):
            st.markdown("#### 👀 Look around and name 5 things you can SEE:")
            see_items = st.text_area("List 5 things you can see:", height=100, key="see_items")
            
            if see_items:
                st.markdown("#### 👂 Listen and name 4 things you can HEAR:")
                hear_items = st.text_area("List 4 things you can hear:", height=80, key="hear_items")
                
                if hear_items:
                    st.markdown("#### ✋ Name 3 things you can TOUCH:")
                    touch_items = st.text_area("List 3 things you can touch:", height=60, key="touch_items")
                    
                    if touch_items:
                        st.markdown("#### 👃 Name 2 things you can SMELL:")
                        smell_items = st.text_area("List 2 things you can smell:", height=60, key="smell_items")
                        
                        if smell_items:
                            st.markdown("#### 👅 Name 1 thing you can TASTE:")
                            taste_item = st.text_input("What can you taste?", key="taste_item")
                            
                            if taste_item:
                                st.success("🎉 Excellent! You've completed the 5-4-3-2-1 grounding exercise. How do you feel now?")
                                
                                feeling_after = st.selectbox(
                                    "How grounded do you feel?",
                                    ["Much more grounded", "Somewhat more grounded", "About the same", "Less grounded"]
                                )
                                
                                if feeling_after:
                                    st.info("Grounding exercises work best with regular practice. Try this whenever you feel anxious or overwhelmed.")
    
    elif exercise_type == "Body Scan Meditation":
        st.markdown("""
        ### 🧘 Body Scan Meditation
        
        A body scan helps you tune into physical sensations and release tension.
        """)
        
        if st.button("🧘 Start Body Scan"):
            st.markdown("""
            **Follow these steps:**
            
            1. **Get comfortable** - Sit or lie down in a comfortable position
            2. **Close your eyes** or soften your gaze
            3. **Start at your toes** - Notice any sensations in your toes
            4. **Move slowly upward** - Gradually move your attention up through your body
            5. **Don't judge** - Simply notice what you feel without trying to change it
            6. **Breathe naturally** - Let your breath flow naturally as you scan
            
            **Take 5-10 minutes to slowly scan from your toes to the top of your head.**
            """)
            
            time.sleep(2)  # Brief pause
            
            st.markdown("#### How was your body scan experience?")
            
            tension_before = st.slider("Tension level before (1-10):", 1, 10, 5, key="tension_before")
            tension_after = st.slider("Tension level after (1-10):", 1, 10, 3, key="tension_after")
            
            if tension_before > tension_after:
                improvement = tension_before - tension_after
                st.success(f"Great! Your tension decreased by {improvement} points! 📉")
    
    elif exercise_type == "Mindful Observation":
        st.markdown("""
        ### 👁️ Mindful Observation
        
        Choose an object and observe it mindfully for 2-3 minutes.
        """)
        
        if st.button("👁️ Start Mindful Observation"):
            st.markdown("""
            **Instructions:**
            
            1. **Choose an object** - Pick something nearby (a pen, plant, coffee cup, etc.)
            2. **Observe like it's the first time** - Pretend you've never seen this object before
            3. **Notice details** - Color, texture, shape, weight, temperature
            4. **Stay curious** - What do you notice that you hadn't before?
            5. **When your mind wanders** - Gently bring attention back to the object
            
            **Spend 2-3 minutes in mindful observation.**
            """)
            
            object_observed = st.text_input("What object did you observe?")
            insights = st.text_area("What did you notice about this object that you hadn't before?", height=100)
            
            if object_observed and insights:
                st.success("🎉 Wonderful! Mindful observation helps train your attention and brings you into the present moment.")

def render_quick_calming():
    """Render quick calming techniques for immediate relief"""
    
    st.subheader("🌱 Quick Calming Techniques")
    st.markdown("When you need immediate relief from stress or anxiety, try these quick techniques.")
    
    # Quick technique cards
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🫁 60-Second Breathing"):
            st.markdown("""
            **Quick Breathing Reset:**
            
            1. Breathe in for 4 counts
            2. Hold for 4 counts  
            3. Breathe out for 6 counts
            4. Repeat for 1 minute
            
            *This activates your relaxation response quickly.*
            """)
            
            # Simple countdown
            if st.button("Start 60-Second Reset"):
                countdown_container = st.empty()
                for i in range(60, 0, -1):
                    countdown_container.markdown(f"### {i} seconds remaining")
                    time.sleep(1)
                countdown_container.markdown("### ✅ Complete!")
                st.success("Great job! How do you feel?")
        
        if st.button("🧊 Ice Cube Technique"):
            st.markdown("""
            **Cold Sensation Grounding:**
            
            1. Hold an ice cube in your hand
            2. Focus on the cold sensation
            3. Notice how it feels as it melts
            4. Let the cold sensation anchor you to the present
            
            *Cold sensations can quickly interrupt anxiety spirals.*
            """)
        
        if st.button("💪 Progressive Muscle Release"):
            st.markdown("""
            **Quick Tension Release:**
            
            1. Tense all your muscles for 5 seconds
            2. Release everything at once
            3. Notice the contrast
            4. Repeat 2-3 times
            
            *This helps release physical tension quickly.*
            """)
    
    with col2:
        if st.button("🔢 Counting Technique"):
            st.markdown("""
            **Distraction Counting:**
            
            - Count backwards from 100 by 7s
            - Or count objects of a specific color
            - Or count your breaths up to 10, then start over
            
            *Counting engages your logical brain and interrupts anxiety.*
            """)
        
        if st.button("🌈 Color Grounding"):
            st.markdown("""
            **Color-Based Grounding:**
            
            1. Pick a color (like blue)
            2. Find 5 things of that color around you
            3. Really focus on each item
            4. Notice different shades and textures
            
            *Visual focus helps calm your nervous system.*
            """)
        
        if st.button("💭 Thought Stopping"):
            st.markdown("""
            **Stop Spiraling Thoughts:**
            
            1. When you notice anxious thoughts, say "STOP"
            2. Take 3 deep breaths
            3. Name 3 things you're grateful for
            4. Choose one positive action to take
            
            *This interrupts negative thought loops.*
            """)
    
    # Emergency coping kit
    st.markdown("---")
    st.subheader("🚨 Emergency Coping Kit")
    st.error("""
    **If you're having a panic attack or severe anxiety:**
    
    🫁 **Breathe slowly** - In for 4, out for 6
    🧊 **Use your senses** - Hold something cold, smell something pleasant
    📱 **Call someone** - Reach out to a trusted person
    🏥 **Seek help** - If symptoms persist, contact a healthcare provider
    🆘 **Crisis resources** - Call 988 or text HOME to 741741
    
    **Remember:** Panic attacks are temporary and will pass. You are safe.
    """)

def render_practice_tracking():
    """Track and display breathing/mindfulness practice history"""
    
    if 'breathing_sessions' not in st.session_state:
        st.session_state.breathing_sessions = []
    
    if not st.session_state.breathing_sessions:
        st.info("🌱 Your breathing and mindfulness practice history will appear here!")
        return
    
    st.subheader("📊 Your Practice History")
    
    # Practice statistics
    total_sessions = len(st.session_state.breathing_sessions)
    total_time = sum(
        {"1 minute": 1, "2 minutes": 2, "5 minutes": 5, "10 minutes": 10}.get(session.get("duration", "1 minute"), 1)
        for session in st.session_state.breathing_sessions
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Sessions", total_sessions)
    
    with col2:
        st.metric("Total Practice Time", f"{total_time} minutes")
    
    with col3:
        if total_sessions > 0:
            avg_per_day = total_sessions / max(1, (datetime.now() - datetime.fromisoformat(st.session_state.breathing_sessions[0]["timestamp"])).days or 1)
            st.metric("Sessions/Day", f"{avg_per_day:.1f}")
    
    # Recent sessions
    st.markdown("### 📅 Recent Sessions")
    
    recent_sessions = sorted(
        st.session_state.breathing_sessions,
        key=lambda x: x["timestamp"],
        reverse=True
    )[:10]
    
    for session in recent_sessions:
        timestamp = datetime.fromisoformat(session["timestamp"])
        
        with st.expander(f"{session['technique']} - {timestamp.strftime('%B %d, %Y at %I:%M %p')}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Duration:** {session['duration']}")
                st.write(f"**Cycles:** {session.get('cycles_completed', 'Unknown')}")
            
            with col2:
                if 'relaxation_after' in session:
                    st.write(f"**Relaxation Level:** {session['relaxation_after']}/10")
                if 'anxiety_after' in session:
                    st.write(f"**Anxiety Level:** {session['anxiety_after']}/10")
    
    # Practice insights
    if len(st.session_state.breathing_sessions) >= 5:
        st.markdown("### 💡 Practice Insights")
        
        # Most used technique
        techniques = [s.get("technique", "Unknown") for s in st.session_state.breathing_sessions]
        most_common = max(set(techniques), key=techniques.count)
        st.write(f"**Favorite technique:** {most_common}")
        
        # Practice consistency
        if total_sessions >= 7:
            st.write(f"**Consistency:** You've been practicing regularly! {total_sessions} sessions total.")
            st.success("🌟 Great job building a consistent practice!")
        
        # Effectiveness tracking
        relaxation_scores = [s.get('relaxation_after') for s in st.session_state.breathing_sessions if 'relaxation_after' in s]
        if relaxation_scores:
            avg_relaxation = sum(relaxation_scores) / len(relaxation_scores)
            st.write(f"**Average relaxation level:** {avg_relaxation:.1f}/10")
            
            if avg_relaxation >= 7:
                st.success("Your breathing practice is helping you achieve good relaxation levels! 🧘")
