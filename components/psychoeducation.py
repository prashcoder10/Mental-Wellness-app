import streamlit as st # type: ignore
from datetime import datetime

def render_psychoeducation():
    """Render mental health education and resources"""
    
    st.header("📚 Learn About Mental Health")
    st.markdown("Knowledge is power. Understanding mental health can help you recognize patterns, develop coping skills, and know when to seek help.")
    
    # Create tabs for different educational content
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🧠 Understanding Mental Health", 
        "😟 Common Challenges", 
        "💪 Coping Strategies", 
        "🆘 When to Seek Help",
        "🌟 Building Resilience"
    ])
    
    with tab1:
        render_mental_health_basics()
    
    with tab2:
        render_common_challenges()
    
    with tab3:
        render_coping_strategies()
    
    with tab4:
        render_when_to_seek_help()
    
    with tab5:
        render_resilience_building()

def render_mental_health_basics():
    """Basic mental health education"""
    
    st.subheader("🧠 Understanding Mental Health")
    
    st.markdown("""
    Mental health includes our emotional, psychological, and social well-being. It affects how we think, 
    feel, and act. It also helps determine how we handle stress, relate to others, and make choices.
    """)
    
    # Mental health myths and facts
    st.markdown("### 🔍 Mental Health: Myths vs. Facts")
    
    myth_fact_data = [
        {
            "myth": "Mental health problems are uncommon among young people",
            "fact": "1 in 5 youth experience a mental health condition. You're not alone."
        },
        {
            "myth": "People with mental health issues are weak or flawed",
            "fact": "Mental health conditions are medical conditions, just like diabetes or asthma."
        },
        {
            "myth": "Therapy is only for people with serious problems",
            "fact": "Therapy can help anyone learn coping skills and improve their well-being."
        },
        {
            "myth": "Mental health problems will go away on their own",
            "fact": "Like physical health, mental health benefits from attention and care."
        },
        {
            "myth": "Asking for help is a sign of weakness",
            "fact": "Seeking help shows strength and self-awareness."
        }
    ]
    
    for item in myth_fact_data:
        with st.expander(f"Myth: {item['myth']}"):
            st.success(f"**Fact:** {item['fact']}")
    
    # What affects mental health
    st.markdown("### 🌊 What Affects Mental Health?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Biological Factors:**")
        st.write("• Genetics and family history")
        st.write("• Brain chemistry")
        st.write("• Hormonal changes")
        st.write("• Medical conditions")
        st.write("• Substance use")
        
        st.markdown("**Environmental Factors:**")
        st.write("• Trauma or abuse")
        st.write("• Significant life changes")
        st.write("• Chronic stress")
        st.write("• Social isolation")
        st.write("• Discrimination")
    
    with col2:
        st.markdown("**Lifestyle Factors:**")
        st.write("• Sleep quality")
        st.write("• Physical activity")
        st.write("• Nutrition")
        st.write("• Social connections")
        st.write("• Coping skills")
        
        st.markdown("**Protective Factors:**")
        st.write("• Strong relationships")
        st.write("• Problem-solving skills")
        st.write("• Self-esteem")
        st.write("• Sense of purpose")
        st.write("• Access to support")
    
    # Mental health spectrum
    st.markdown("### 📊 The Mental Health Spectrum")
    
    st.info("""
    Mental health exists on a spectrum - it's not just "healthy" or "unhealthy." We all move along this spectrum throughout our lives:
    
    🌟 **Thriving** - Feeling great, handling challenges well
    
    😊 **Doing Well** - Generally good mood, occasional stress
    
    😐 **Getting By** - Some challenges, manageable stress
    
    😟 **Struggling** - Frequent difficulties, increased stress
    
    🆘 **In Crisis** - Unable to cope, need immediate support
    
    **Remember:** It's normal to move along this spectrum. The goal is to develop skills to move toward thriving.
    """)

def render_common_challenges():
    """Information about common mental health challenges for youth"""
    
    st.subheader("😟 Common Mental Health Challenges")
    st.markdown("Many young people experience these challenges. Understanding them can help you recognize when you or someone you know might need support.")
    
    # Common conditions
    conditions = {
        "Anxiety": {
            "icon": "😰",
            "description": "Persistent worry or fear that interferes with daily activities",
            "symptoms": [
                "Excessive worry about future events",
                "Physical symptoms like rapid heartbeat or sweating",
                "Avoiding situations that cause anxiety",
                "Difficulty concentrating",
                "Sleep problems",
                "Feeling restless or on edge"
            ],
            "help": [
                "Practice breathing exercises and mindfulness",
                "Challenge negative thoughts",
                "Gradually face feared situations",
                "Maintain regular exercise and sleep",
                "Talk to a trusted adult or counselor"
            ]
        },
        "Depression": {
            "icon": "😢",
            "description": "Persistent feelings of sadness, hopelessness, or loss of interest",
            "symptoms": [
                "Feeling sad, empty, or hopeless most days",
                "Loss of interest in activities once enjoyed",
                "Changes in appetite or weight",
                "Sleep problems (too much or too little)",
                "Fatigue or loss of energy",
                "Difficulty concentrating or making decisions",
                "Feelings of worthlessness or guilt"
            ],
            "help": [
                "Maintain connections with friends and family",
                "Keep a regular routine",
                "Engage in activities you used to enjoy",
                "Practice self-care and self-compassion",
                "Seek professional help if symptoms persist"
            ]
        },
        "Stress": {
            "icon": "😤",
            "description": "The body's response to challenges or demands",
            "symptoms": [
                "Feeling overwhelmed or pressured",
                "Irritability or mood swings",
                "Physical tension or headaches",
                "Difficulty sleeping",
                "Changes in appetite",
                "Trouble concentrating"
            ],
            "help": [
                "Identify and manage stressors",
                "Practice time management",
                "Use relaxation techniques",
                "Exercise regularly",
                "Talk to someone about your stress",
                "Break large tasks into smaller steps"
            ]
        },
        "Social Anxiety": {
            "icon": "😳",
            "description": "Intense fear of social situations and being judged by others",
            "symptoms": [
                "Fear of embarrassment in social situations",
                "Avoiding social gatherings or speaking up",
                "Physical symptoms in social situations",
                "Worrying about social events days in advance",
                "Fear of being the center of attention"
            ],
            "help": [
                "Start with small social interactions",
                "Practice social skills in low-pressure situations",
                "Challenge negative thoughts about social situations",
                "Use grounding techniques in social settings",
                "Consider therapy focused on social anxiety"
            ]
        }
    }
    
    # Display condition information
    selected_condition = st.selectbox(
        "Learn more about:",
        list(conditions.keys())
    )
    
    condition_info = conditions[selected_condition]
    
    st.markdown(f"## {condition_info['icon']} {selected_condition}")
    st.write(condition_info['description'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔍 Common Signs:")
        for symptom in condition_info['symptoms']:
            st.write(f"• {symptom}")
    
    with col2:
        st.markdown("### 💡 What Can Help:")
        for help_item in condition_info['help']:
            st.write(f"• {help_item}")
    
    # Important note
    st.warning("""
    **Important:** These are general descriptions. If you're experiencing several of these symptoms for more than two weeks, 
    or if they're significantly impacting your daily life, please talk to a trusted adult, counselor, or healthcare provider.
    """)
    
    # Self-assessment disclaimer
    st.markdown("### 📋 Quick Self-Check")
    st.info("""
    While this chatbot can provide support and information, it cannot diagnose mental health conditions. 
    If you're concerned about your mental health, consider:
    
    • Talking to a school counselor
    • Speaking with your doctor
    • Contacting a mental health professional
    • Calling a mental health helpline
    
    **Crisis Resources:**
    • 988 - Suicide & Crisis Lifeline
    • Text HOME to 741741 - Crisis Text Line
    """)

def render_coping_strategies():
    """Evidence-based coping strategies and techniques"""
    
    st.subheader("💪 Healthy Coping Strategies")
    st.markdown("Learn practical strategies to manage stress, difficult emotions, and challenging situations.")
    
    # Coping strategy categories
    strategy_tabs = st.tabs(["🧘 Emotional Coping", "🎯 Problem-Focused", "🤝 Social Support", "🏃 Physical Wellness"])
    
    with strategy_tabs[0]:
        st.markdown("### 🧘 Emotional Coping Strategies")
        st.markdown("These help you manage difficult emotions and stress:")
        
        emotional_strategies = [
            {
                "name": "Deep Breathing",
                "description": "Slow, intentional breathing to activate your body's relaxation response",
                "how_to": "Breathe in for 4 counts, hold for 4, exhale for 6. Repeat 5-10 times."
            },
            {
                "name": "Mindfulness",
                "description": "Staying present and aware without judgment",
                "how_to": "Focus on your breath, body sensations, or surroundings. When your mind wanders, gently return focus."
            },
            {
                "name": "Journaling",
                "description": "Writing about your thoughts and feelings to process emotions",
                "how_to": "Write freely about what you're experiencing. Don't worry about grammar or structure."
            },
            {
                "name": "Progressive Muscle Relaxation",
                "description": "Tensing and relaxing muscle groups to release physical tension",
                "how_to": "Tense each muscle group for 5 seconds, then relax. Start with your toes and work up."
            },
            {
                "name": "Grounding Techniques",
                "description": "Using your senses to connect with the present moment",
                "how_to": "Name 5 things you see, 4 you hear, 3 you touch, 2 you smell, 1 you taste."
            }
        ]
        
        for strategy in emotional_strategies:
            with st.expander(f"💡 {strategy['name']}"):
                st.write(strategy['description'])
                st.markdown(f"**How to do it:** {strategy['how_to']}")
    
    with strategy_tabs[1]:
        st.markdown("### 🎯 Problem-Focused Coping")
        st.markdown("These help you actively address challenges:")
        
        problem_strategies = [
            {
                "name": "Problem-Solving Steps",
                "steps": [
                    "Define the problem clearly",
                    "Brainstorm possible solutions",
                    "Evaluate pros and cons of each option",
                    "Choose the best solution",
                    "Make an action plan",
                    "Try it out and evaluate results"
                ]
            },
            {
                "name": "Time Management",
                "steps": [
                    "Make a daily or weekly schedule",
                    "Prioritize tasks (urgent vs. important)",
                    "Break large tasks into smaller steps",
                    "Set realistic deadlines",
                    "Take regular breaks",
                    "Celebrate completed tasks"
                ]
            },
            {
                "name": "Setting Boundaries",
                "steps": [
                    "Identify your limits and needs",
                    "Communicate clearly and kindly",
                    "Practice saying 'no' when necessary",
                    "Be consistent with your boundaries",
                    "Take care of yourself first",
                    "Ask for support when needed"
                ]
            }
        ]
        
        for strategy in problem_strategies:
            st.markdown(f"**{strategy['name']}:**")
            for i, step in enumerate(strategy['steps'], 1):
                st.write(f"{i}. {step}")
            st.write("---")
    
    with strategy_tabs[2]:
        st.markdown("### 🤝 Social Support Strategies")
        st.markdown("Building and using your support network:")
        
        st.markdown("""
        **Building Your Support Network:**
        • Identify trusted friends, family members, teachers, or counselors
        • Join clubs, groups, or activities that interest you
        • Volunteer for causes you care about
        • Be a good friend to others
        • Practice active listening and empathy
        
        **When You Need Support:**
        • Reach out before things get overwhelming
        • Be specific about what kind of help you need
        • Accept help when it's offered
        • Express gratitude for support received
        • Remember that asking for help is a sign of strength
        
        **Supporting Others:**
        • Listen without trying to "fix" everything
        • Offer specific help ("Can I help with homework?")
        • Check in regularly
        • Encourage professional help when needed
        • Take care of your own well-being too
        """)
    
    with strategy_tabs[3]:
        st.markdown("### 🏃 Physical Wellness Strategies")
        st.markdown("Taking care of your body supports mental health:")
        
        physical_strategies = {
            "Exercise": "Regular physical activity releases endorphins and reduces stress. Even 10-15 minutes of walking can help.",
            "Sleep Hygiene": "Aim for 8-9 hours of sleep. Keep a regular schedule, avoid screens before bed, create a relaxing environment.",
            "Nutrition": "Eat regular, balanced meals. Stay hydrated. Limit caffeine and sugar which can increase anxiety.",
            "Nature Time": "Spending time outdoors can reduce stress and improve mood. Even looking at nature through a window helps.",
            "Creative Expression": "Art, music, writing, dance, or crafts can be therapeutic outlets for emotions.",
            "Relaxation Activities": "Reading, taking baths, listening to music, or other calming activities you enjoy."
        }
        
        for strategy, description in physical_strategies.items():
            st.markdown(f"**{strategy}:** {description}")
        
        st.info("""
        **Remember:** What works for one person might not work for another. Try different strategies and find what helps you most. 
        It's also okay to use different strategies for different situations.
        """)

def render_when_to_seek_help():
    """Guidelines for when and how to seek professional help"""
    
    st.subheader("🆘 When to Seek Help")
    st.markdown("Knowing when and how to get help is an important life skill. You don't have to handle everything alone.")
    
    # When to seek help
    st.markdown("### 🚨 It's Time to Seek Help When:")
    
    warning_signs = [
        "Your symptoms last for more than two weeks",
        "Your daily activities are significantly impacted",
        "You're having thoughts of self-harm or suicide",
        "You're using substances to cope",
        "You've experienced trauma or abuse",
        "Friends or family are expressing concern",
        "You feel hopeless or like nothing will ever get better",
        "You're having panic attacks or severe anxiety",
        "Your eating or sleeping patterns have changed drastically",
        "You feel disconnected from reality"
    ]
    
    for sign in warning_signs:
        st.write(f"• {sign}")
    
    st.error("""
    **Immediate Crisis Signs - Get Help Now:**
    • Thoughts of suicide or self-harm
    • Plans to hurt yourself or others
    • Hearing voices or seeing things others don't
    • Feeling completely out of control
    • Severe panic that won't stop
    
    **Call 911 or go to the emergency room immediately**
    """)
    
    # Types of help available
    st.markdown("### 🏥 Types of Help Available")
    
    help_types = {
        "School Counselor": {
            "description": "Trained professionals at your school who can provide support and connect you with resources",
            "good_for": "Academic stress, peer issues, family problems, mental health concerns",
            "how_to": "Visit the counseling office or ask a teacher to help you make an appointment"
        },
        "Therapist/Counselor": {
            "description": "Licensed mental health professionals who provide counseling and therapy",
            "good_for": "Depression, anxiety, trauma, relationship issues, coping skills",
            "how_to": "Ask your doctor for a referral, check with your insurance, or search online directories"
        },
        "Psychiatrist": {
            "description": "Medical doctors who can prescribe medication and provide therapy",
            "good_for": "Severe symptoms, medication management, complex mental health conditions",
            "how_to": "Get a referral from your primary care doctor or therapist"
        },
        "Primary Care Doctor": {
            "description": "Your regular doctor can help with mental health concerns and provide referrals",
            "good_for": "Initial assessment, medication, physical symptoms of mental health issues",
            "how_to": "Schedule an appointment and be honest about your mental health concerns"
        },
        "Crisis Hotlines": {
            "description": "24/7 support lines staffed by trained counselors",
            "good_for": "Immediate crisis, suicidal thoughts, need someone to talk to right now",
            "how_to": "Call 988 (Suicide & Crisis Lifeline) or text HOME to 741741 (Crisis Text Line)"
        }
    }
    
    selected_help = st.selectbox("Learn more about:", list(help_types.keys()))
    
    help_info = help_types[selected_help]
    st.markdown(f"**{selected_help}:**")
    st.write(help_info['description'])
    st.write(f"**Good for:** {help_info['good_for']}")
    st.write(f"**How to access:** {help_info['how_to']}")
    
    # Preparing for help
    st.markdown("### 📝 Preparing to Ask for Help")
    
    st.info("""
    **Before your appointment or conversation:**
    
    • Write down your symptoms and when they started
    • Note what makes them better or worse
    • List any medications you're taking
    • Think about your goals for treatment
    • Prepare questions you want to ask
    • Consider bringing a trusted person for support
    
    **What to expect:**
    • The professional will ask about your symptoms and history
    • They may ask about family mental health history
    • Everything you share is confidential (with rare exceptions for safety)
    • Treatment often involves both therapy and sometimes medication
    • It may take time to find the right treatment approach
    """)
    
    # Overcoming barriers
    st.markdown("### 🚧 Overcoming Common Barriers")
    
    barriers = {
        "\"I don't want to be a burden\"": "Getting help is taking responsibility for your well-being. Mental health professionals are there to help - it's their job and passion.",
        "\"My problems aren't serious enough\"": "You don't need to be in crisis to deserve help. Prevention and early intervention are always better.",
        "\"I should be able to handle this alone\"": "Everyone needs help sometimes. Asking for help shows strength and maturity.",
        "\"I'm worried about confidentiality\"": "Mental health professionals are bound by strict confidentiality rules. They can only break confidentiality in rare cases involving immediate danger.",
        "\"I can't afford therapy\"": "Many options exist: school counselors, community mental health centers, sliding scale fees, insurance coverage, and online resources.",
        "\"My parents won't understand\"": "Try explaining how you're feeling and that you want to get better. Many parents want to help but don't know how."
    }
    
    for barrier, response in barriers.items():
        with st.expander(barrier):
            st.write(response)

def render_resilience_building():
    """Information and activities for building mental resilience"""
    
    st.subheader("🌟 Building Resilience")
    st.markdown("Resilience is your ability to bounce back from challenges. It's a skill you can develop and strengthen over time.")
    
    # What is resilience
    st.markdown("### 🏗️ What is Resilience?")
    
    st.info("""
    **Resilience is NOT:**
    • Being happy all the time
    • Never feeling stressed or sad
    • Handling everything perfectly
    • Being invulnerable to problems
    
    **Resilience IS:**
    • Adapting well to adversity and stress
    • Learning from challenges and setbacks
    • Maintaining hope during difficult times
    • Having effective coping strategies
    • Being able to ask for help when needed
    • Growing stronger through experiences
    """)
    
    # Resilience factors
    st.markdown("### 🧱 Building Blocks of Resilience")
    
    resilience_tabs = st.tabs(["🧠 Mental Skills", "❤️ Emotional Skills", "🤝 Social Skills", "🎯 Life Skills"])
    
    with resilience_tabs[0]:
        st.markdown("**Mental/Cognitive Skills:**")
        mental_skills = [
            "**Problem-solving:** Break big problems into smaller, manageable steps",
            "**Flexible thinking:** Consider multiple perspectives and solutions",
            "**Realistic optimism:** Maintain hope while being realistic about challenges",
            "**Self-awareness:** Understand your thoughts, feelings, and reactions",
            "**Growth mindset:** Believe that abilities can be developed through effort",
            "**Meaning-making:** Find purpose and meaning in experiences"
        ]
        
        for skill in mental_skills:
            st.write(f"• {skill}")
        
        st.markdown("**💡 Practice Activity:**")
        st.markdown("Think of a recent challenge. How could you view it as a learning opportunity? What skills did you develop or strengthen?")
    
    with resilience_tabs[1]:
        st.markdown("**Emotional Skills:**")
        emotional_skills = [
            "**Emotional awareness:** Recognize and name your emotions",
            "**Emotional regulation:** Manage intense emotions in healthy ways",
            "**Self-compassion:** Treat yourself with kindness during difficult times",
            "**Stress management:** Use healthy coping strategies for stress",
            "**Acceptance:** Accept what you cannot change while working on what you can",
            "**Gratitude:** Focus on positive aspects of life, even during hardship"
        ]
        
        for skill in emotional_skills:
            st.write(f"• {skill}")
        
        st.markdown("**💡 Practice Activity:**")
        st.markdown("Start a daily gratitude practice. Each day, write down three things you're grateful for, no matter how small.")
    
    with resilience_tabs[2]:
        st.markdown("**Social Skills:**")
        social_skills = [
            "**Communication:** Express needs, feelings, and boundaries clearly",
            "**Empathy:** Understand and connect with others' experiences",
            "**Relationship building:** Develop and maintain supportive relationships",
            "**Help-seeking:** Know when and how to ask for support",
            "**Community connection:** Feel connected to groups or causes larger than yourself",
            "**Social support:** Give and receive emotional and practical support"
        ]
        
        for skill in social_skills:
            st.write(f"• {skill}")
        
        st.markdown("**💡 Practice Activity:**")
        st.markdown("Reach out to someone you care about today. Ask how they're doing and really listen to their response.")
    
    with resilience_tabs[3]:
        st.markdown("**Life Skills:**")
        life_skills = [
            "**Goal setting:** Set realistic, achievable goals and work toward them",
            "**Time management:** Balance responsibilities with self-care",
            "**Self-care:** Take care of physical, mental, and emotional needs",
            "**Healthy habits:** Maintain routines that support well-being",
            "**Adaptability:** Adjust to change and uncertainty",
            "**Future planning:** Think ahead while staying present"
        ]
        
        for skill in life_skills:
            st.write(f"• {skill}")
        
        st.markdown("**💡 Practice Activity:**")
        st.markdown("Set one small, achievable goal for this week. Make a plan for how you'll accomplish it, then celebrate when you do!")
    
    # Resilience building activities
    st.markdown("### 🎯 Resilience-Building Activities")
    
    activities = {
        "Daily Reflection": "Spend 5 minutes each evening reflecting on what went well and what you learned",
        "Challenge Reframing": "When facing a problem, ask 'How might this help me grow?' or 'What can I learn from this?'",
        "Strengths Inventory": "Make a list of your strengths and past successes to remind yourself of your capabilities",
        "Support Network Map": "Identify people you can turn to for different types of support",
        "Future Self Visualization": "Imagine yourself successfully handling future challenges",
        "Acts of Kindness": "Help others to build connection and purpose",
        "Learning New Skills": "Challenge yourself to learn something new to build confidence",
        "Mindfulness Practice": "Regular mindfulness helps with emotional regulation and stress management"
    }
    
    selected_activity = st.selectbox("Try a resilience-building activity:", list(activities.keys()))
    st.info(f"**{selected_activity}:** {activities[selected_activity]}")
    
    # Personal resilience plan
    st.markdown("### 📋 Your Personal Resilience Plan")
    
    if st.button("🌟 Create My Resilience Plan"):
        st.markdown("**Answer these questions to create your personal resilience plan:**")
        
        with st.form("resilience_plan"):
            st.markdown("**1. My Strengths:**")
            strengths = st.text_area("What are you good at? What do others appreciate about you?", height=80)
            
            st.markdown("**2. My Support Network:**")
            support = st.text_area("Who can you turn to for help? (friends, family, teachers, etc.)", height=80)
            
            st.markdown("**3. My Coping Strategies:**")
            coping = st.text_area("What helps you feel better when you're stressed or upset?", height=80)
            
            st.markdown("**4. My Goals:**")
            goals = st.text_area("What do you want to work on or achieve?", height=80)
            
            st.markdown("**5. My Self-Care:**")
            self_care = st.text_area("How do you take care of yourself physically and emotionally?", height=80)
            
            if st.form_submit_button("💾 Create My Plan"):
                plan = f"""
# My Personal Resilience Plan

**My Strengths:** {strengths}

**My Support Network:** {support}

**My Coping Strategies:** {coping}

**My Goals:** {goals}

**My Self-Care:** {self_care}

**Reminder:** Resilience is built over time. Be patient with yourself and celebrate small progress!
                """
                
                st.success("Your resilience plan has been created!")
                st.download_button(
                    label="📄 Download My Resilience Plan",
                    data=plan,
                    file_name=f"resilience_plan_{datetime.now().strftime('%Y%m%d')}.md",
                    mime="text/markdown"
                )
    
    # Resilience reminders
    st.markdown("### 💭 Remember")
    
    st.success("""
    🌟 **Resilience Reminders:**
    
    • Resilience is a skill that can be learned and strengthened
    • It's okay to struggle - that's how we grow
    • Small steps count - you don't have to change everything at once
    • Everyone's resilience looks different
    • It's okay to have bad days
    • Asking for help is a sign of strength
    • You are stronger than you think
    • This too shall pass
    """)
