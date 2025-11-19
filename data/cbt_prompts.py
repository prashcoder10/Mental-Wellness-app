"""
CBT exercises, prompts, and cognitive distortion definitions
Based on evidence-based Cognitive Behavioral Therapy techniques
"""

# Comprehensive CBT exercises organized by type and difficulty
CBT_EXERCISES = {
    "thought_records": {
        "basic": [
            "Identify a situation that caused you stress today. What automatic thoughts came up?",
            "Think of a time you felt anxious. What was going through your mind?",
            "Describe a moment when you felt disappointed. What thoughts contributed to that feeling?",
            "Recall a situation where you felt angry. What thoughts fueled that anger?"
        ],
        "intermediate": [
            "Think of a recurring worry. What evidence supports this worry? What evidence challenges it?",
            "Identify a negative thought about yourself. How would you challenge this thought?",
            "Consider a situation you're avoiding. What thoughts are keeping you from facing it?",
            "Reflect on a recent conflict. What assumptions did you make about the other person's intentions?"
        ],
        "advanced": [
            "Analyze a pattern of negative thinking you've noticed. What triggers these thoughts?",
            "Examine a core belief about yourself. How has this belief shaped your experiences?",
            "Identify a situation where you catastrophized. How could you think about it more realistically?",
            "Consider a time you mind-read or predicted negative outcomes. What was the actual result?"
        ]
    },
    
    "behavioral_experiments": {
        "social_anxiety": [
            "Ask a question in class or during a meeting",
            "Make small talk with a cashier or service worker",
            "Express a different opinion in a group conversation",
            "Attend a social event for at least 30 minutes",
            "Initiate plans with a friend or acquaintance"
        ],
        "depression": [
            "Engage in one activity you used to enjoy for 15 minutes",
            "Reach out to one person you haven't talked to in a while",
            "Complete one small task you've been putting off",
            "Go for a 10-minute walk outside",
            "Do one kind thing for yourself today"
        ],
        "general_anxiety": [
            "Practice a new skill for 10 minutes",
            "Visit a place that makes you slightly anxious",
            "Try a new food or restaurant",
            "Speak up in a situation where you normally stay quiet",
            "Do something spontaneous and unplanned"
        ]
    },
    
    "cognitive_restructuring": [
        "What would I tell a friend in this exact situation?",
        "What's the most realistic outcome, not the worst-case scenario?",
        "What evidence do I have that contradicts this negative thought?",
        "How will this matter in 5 years? In 1 year? In 1 month?",
        "What would someone who cares about me say about this thought?",
        "Is this thought helping me or hurting me?",
        "What's a more balanced way to look at this situation?",
        "Am I focusing on the negative and ignoring the positive?",
        "What assumptions am I making that might not be true?",
        "How might someone else interpret this situation differently?"
    ],
    
    "activity_scheduling": [
        "Schedule one pleasant activity for each day this week",
        "Plan a balance of necessary tasks and enjoyable activities",
        "Identify activities that give you a sense of accomplishment",
        "Schedule time for activities that connect you with others",
        "Plan activities that align with your values and goals",
        "Include both active and restful activities in your schedule",
        "Schedule regular self-care activities throughout the week"
    ]
}

# Comprehensive cognitive distortions with examples and challenges
COGNITIVE_DISTORTIONS = {
    "All-or-Nothing Thinking": {
        "description": "Seeing things in absolute terms without recognizing middle ground",
        "example": "I made one mistake, so I'm a complete failure",
        "challenge": "Look for the middle ground. What evidence shows this isn't completely true?",
        "alternative": "I made a mistake, but that doesn't define my entire worth or ability"
    },
    
    "Overgeneralization": {
        "description": "Drawing broad conclusions from a single event",
        "example": "I didn't get this job, so I'll never find employment",
        "challenge": "Is this one event really proof of a never-ending pattern?",
        "alternative": "This particular job wasn't the right fit, but other opportunities exist"
    },
    
    "Mental Filter": {
        "description": "Focusing exclusively on negative details while ignoring positive aspects",
        "example": "My presentation was terrible because I stumbled over one word",
        "challenge": "What positive aspects am I overlooking? What went well?",
        "alternative": "I stumbled once, but overall my presentation was well-received"
    },
    
    "Discounting the Positive": {
        "description": "Dismissing positive experiences as unimportant or not counting",
        "example": "My friend complimented me, but they were just being nice",
        "challenge": "Why am I dismissing this positive feedback? Could it be genuine?",
        "alternative": "My friend took time to give me a compliment, which suggests they meant it"
    },
    
    "Jumping to Conclusions": {
        "description": "Making negative assumptions without evidence",
        "subtypes": {
            "Mind Reading": "They think I'm boring",
            "Fortune Telling": "I know I'll fail this test"
        },
        "challenge": "What evidence do I actually have for this conclusion?",
        "alternative": "I don't know what they're thinking. Let me focus on what I can control"
    },
    
    "Magnification/Minimization": {
        "description": "Exaggerating negatives or downplaying positives",
        "example": "This mistake is catastrophic, but my successes don't really matter",
        "challenge": "Am I blowing this out of proportion or shrinking something important?",
        "alternative": "This is a setback, but it's manageable and I can learn from it"
    },
    
    "Emotional Reasoning": {
        "description": "Believing feelings reflect reality",
        "example": "I feel like a failure, so I must be one",
        "challenge": "Are my feelings always accurate reflections of reality?",
        "alternative": "I feel bad right now, but feelings aren't facts"
    },
    
    "Should Statements": {
        "description": "Having rigid rules about how things should be",
        "example": "I should never make mistakes" or "People should always be fair",
        "challenge": "Who made this rule? Is it realistic or helpful?",
        "alternative": "I prefer when things go smoothly, but mistakes are part of being human"
    },
    
    "Labeling": {
        "description": "Defining yourself or others by a single characteristic",
        "example": "I'm an idiot (instead of: I made a mistake)",
        "challenge": "Am I defining myself by one action or trait?",
        "alternative": "I acted in a way I regret, but that doesn't define who I am"
    },
    
    "Personalization": {
        "description": "Taking responsibility for things outside your control",
        "example": "My friend is upset, so it must be something I did",
        "challenge": "What else could be causing this situation?",
        "alternative": "There could be many reasons they're upset that have nothing to do with me"
    },
    
    "Catastrophizing": {
        "description": "Expecting the worst possible outcome",
        "example": "If I fail this test, I'll never graduate and my life will be ruined",
        "challenge": "What's the most likely outcome? What's the best case scenario?",
        "alternative": "If I don't do well, I can retake it or get extra help"
    },
    
    "Control Fallacies": {
        "description": "Feeling either completely powerless or totally responsible",
        "external": "I can't do anything about this situation",
        "internal": "Everyone's happiness depends on me",
        "challenge": "What aspects can I control? What aspects are outside my control?",
        "alternative": "I can control my actions and responses, but not everything else"
    }
}

# Thought challenging questions organized by category
THOUGHT_CHALLENGING_QUESTIONS = {
    "evidence_based": [
        "What evidence supports this thought?",
        "What evidence contradicts this thought?",
        "If I were a scientist, what would I conclude based on the evidence?",
        "What would I need to see to believe the opposite?",
        "Am I confusing a thought with a fact?"
    ],
    
    "perspective_taking": [
        "How would I view this if it happened to my best friend?",
        "What would a trusted friend or family member say about this thought?",
        "How might someone from a different culture view this situation?",
        "What would I have thought about this a year ago?",
        "How might I view this when I'm feeling better?"
    ],
    
    "time_perspective": [
        "How will this matter in 5 years?",
        "How will this matter in 1 year?",
        "How will this matter in 1 month?",
        "How will this matter in 1 week?",
        "Will I even remember this in a few years?"
    ],
    
    "probability_assessment": [
        "What's the worst thing that could happen?",
        "What's the best thing that could happen?",
        "What's most likely to actually happen?",
        "How often has my worst-case scenario actually come true?",
        "What are the odds this will happen the way I'm imagining?"
    ],
    
    "usefulness": [
        "Is this thought helping me or hurting me?",
        "What would I gain by believing this thought?",
        "What might I lose by holding onto this thought?",
        "Does this thought motivate me or paralyze me?",
        "Is this thought moving me toward or away from my goals?"
    ],
    
    "cognitive_distortion_check": [
        "Am I falling into any thinking traps?",
        "Am I thinking in all-or-nothing terms?",
        "Am I focusing only on the negative?",
        "Am I predicting the future or mind-reading?",
        "Am I personalizing something that isn't about me?"
    ]
}

# Behavioral activation activities by category
BEHAVIORAL_ACTIVATION = {
    "pleasure_activities": [
        "Listen to favorite music",
        "Watch a funny video or movie",
        "Take a warm bath or shower",
        "Spend time in nature",
        "Play with a pet",
        "Read something enjoyable",
        "Do a creative activity (draw, write, craft)",
        "Call or text someone you care about",
        "Look at photos that make you smile",
        "Practice a hobby you enjoy"
    ],
    
    "mastery_activities": [
        "Organize a small space",
        "Learn something new for 15 minutes",
        "Complete a task you've been avoiding",
        "Cook a healthy meal",
        "Exercise for 10-15 minutes",
        "Practice a skill you want to develop",
        "Help someone with something",
        "Plan something you're looking forward to",
        "Work on a personal goal",
        "Fix or improve something"
    ],
    
    "social_activities": [
        "Reach out to a friend or family member",
        "Join a group or club activity",
        "Attend a social event",
        "Collaborate on a project",
        "Volunteer for a cause you care about",
        "Participate in online communities",
        "Meet new people through shared interests",
        "Spend quality time with loved ones",
        "Engage in group exercise or sports",
        "Participate in community events"
    ],
    
    "routine_activities": [
        "Maintain a regular sleep schedule",
        "Eat regular, nutritious meals",
        "Keep up with personal hygiene",
        "Maintain your living space",
        "Complete work or school tasks",
        "Pay bills and handle responsibilities",
        "Plan your day or week",
        "Engage in regular exercise",
        "Practice mindfulness or meditation",
        "Set and work toward goals"
    ]
}

# Values clarification exercises
VALUES_EXERCISES = [
    "What activities make you feel most alive and engaged?",
    "What would you want to be remembered for?",
    "What causes or issues do you care deeply about?",
    "When do you feel most proud of yourself?",
    "What kind of person do you want to be in relationships?",
    "What matters most to you in your work or school life?",
    "How do you want to contribute to your community?",
    "What principles guide your decisions?",
    "What activities align with your core beliefs?",
    "What would you do if you knew you couldn't fail?"
]

# Goal-setting framework (SMART goals)
GOAL_SETTING_FRAMEWORK = {
    "specific": "What exactly do you want to accomplish?",
    "measurable": "How will you know when you've achieved it?",
    "achievable": "Is this realistic given your current situation?",
    "relevant": "Does this align with your values and priorities?",
    "time_bound": "When do you want to accomplish this by?"
}

# Weekly mood and activity monitoring prompts
MOOD_ACTIVITY_MONITORING = [
    "Rate your mood each day from 1-10",
    "Note what activities you engaged in",
    "Identify what activities improved your mood",
    "Notice patterns between activities and mood",
    "Track sleep, exercise, and social interaction",
    "Note any significant events or stressors",
    "Identify your most and least productive times of day"
]
