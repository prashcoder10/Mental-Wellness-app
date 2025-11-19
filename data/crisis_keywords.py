"""
Crisis detection keywords and patterns based on evidence-based research
Reference: Mental health chatbot crisis detection implementation best practices 2025
"""

# Crisis keywords organized by severity and category
CRISIS_KEYWORDS = {
    "suicidal_ideation": [
        "suicide", "kill myself", "end my life", "take my own life", "don't want to live",
        "better off dead", "end it all", "can't go on", "want to die", "wish I was dead",
        "not worth living", "end the pain", "permanent solution", "suicide plan",
        "ways to die", "how to kill", "ending my life", "taking my life"
    ],
    
    "self_harm": [
        "cut myself", "hurt myself", "self harm", "self-harm", "cutting", "burning myself",
        "scratch myself", "hit myself", "punch myself", "self injury", "self-injury",
        "harm my body", "damage myself", "self mutilation", "razor", "blade"
    ],
    
    "severe_depression": [
        "completely hopeless", "no point", "nothing matters", "empty inside",
        "can't feel anything", "numb", "worthless", "useless", "burden to everyone",
        "everyone hates me", "no one cares", "life is meaningless", "can't take it anymore",
        "given up", "too hard", "can't cope", "breaking point"
    ],
    
    "crisis_indicators": [
        "emergency", "crisis", "can't breathe", "panic attack", "losing control",
        "going crazy", "losing my mind", "can't stop", "help me", "scared",
        "terrified", "overwhelmed", "drowning", "suffocating", "trapped"
    ],
    
    "substance_abuse": [
        "overdose", "pills", "drinking too much", "getting high", "drugs", "alcohol",
        "substance", "escape reality", "numb the pain", "self medicate"
    ],
    
    "eating_disorders": [
        "starve myself", "don't deserve food", "hate my body", "too fat", "disgusting",
        "purge", "throw up", "binge", "restrict", "not eating", "lose weight fast"
    ],
    
    "abuse_trauma": [
        "being hurt", "someone hurts me", "abuse", "trauma", "violence", "assault",
        "unsafe", "threatened", "scared at home", "afraid of", "being attacked"
    ],
    
    "psychosis_indicators": [
        "hearing voices", "seeing things", "not real", "hallucination", "paranoid",
        "they're watching", "conspiracy", "following me", "out to get me"
    ]
}

# Severity weights for risk assessment scoring
SEVERITY_WEIGHTS = {
    "suicidal_ideation": 5,      # Highest priority
    "self_harm": 4,              # Very high priority
    "psychosis_indicators": 4,    # Very high priority
    "severe_depression": 3,       # High priority
    "crisis_indicators": 3,       # High priority
    "abuse_trauma": 3,           # High priority
    "substance_abuse": 2,        # Moderate priority
    "eating_disorders": 2        # Moderate priority
}

# Positive indicators that might reduce risk
PROTECTIVE_FACTORS = [
    "getting help", "therapy", "counselor", "support", "family", "friends",
    "hope", "better tomorrow", "trying", "working on it", "getting better",
    "medication", "treatment", "doctor", "professional help"
]

# Context patterns that might indicate higher risk
HIGH_RISK_PATTERNS = [
    r"\b(tonight|today|right now|immediately|can't wait)\b.*\b(suicide|kill|die|end)\b",
    r"\b(plan|planning|decided|going to)\b.*\b(suicide|kill myself|end my life)\b",
    r"\b(pills|rope|gun|bridge|jump)\b.*\b(suicide|kill|die)\b",
    r"\b(final|last|goodbye|farewell)\b.*\b(message|time|chance)\b",
    r"\b(can't take|won't make it|end of the line)\b.*\b(anymore|through this)\b"
]

# Phrases that indicate immediate intervention needed
IMMEDIATE_CRISIS_PHRASES = [
    "I'm going to kill myself",
    "I want to end my life today",
    "I have a plan to die",
    "I'm going to hurt myself now",
    "This is my final message",
    "Goodbye forever",
    "I can't take another minute",
    "I'm going to do it tonight",
    "I have the pills ready",
    "Nobody can stop me"
]

# Follow-up questions for crisis assessment
CRISIS_ASSESSMENT_QUESTIONS = {
    "suicidal_ideation": [
        "Are you thinking about hurting yourself or ending your life?",
        "Do you have a plan for how you would hurt yourself?",
        "Do you have access to means to hurt yourself?",
        "Have you thought about when you might do this?",
        "Is there anything that would stop you?"
    ],
    
    "safety_planning": [
        "Who are the people you trust most in your life?",
        "What activities help you feel calmer?",
        "What are your reasons for living?",
        "Where can you go to feel safe?",
        "Who can you call when you feel this way?"
    ]
}

# Resources and referrals by crisis type
CRISIS_RESOURCES = {
    "suicide_prevention": {
        "primary": "988 Suicide & Crisis Lifeline",
        "text": "Text HOME to 741741",
        "chat": "suicidepreventionlifeline.org",
        "emergency": "Call 911 if in immediate danger"
    },
    
    "abuse_trauma": {
        "domestic_violence": "1-800-799-7233 (National Domestic Violence Hotline)",
        "sexual_assault": "1-800-656-4673 (RAINN National Sexual Assault Hotline)",
        "child_abuse": "1-800-4-A-CHILD (1-800-422-4453)"
    },
    
    "substance_abuse": {
        "samhsa": "1-800-662-4357 (SAMHSA National Helpline)",
        "website": "findtreatment.gov"
    },
    
    "eating_disorders": {
        "neda": "1-800-931-2237 (NEDA Helpline)",
        "crisis": "Text NEDA to 741741"
    }
}

# De-escalation phrases and responses
DE_ESCALATION_RESPONSES = [
    "I can hear that you're in a lot of pain right now.",
    "Thank you for trusting me with these feelings.",
    "You're not alone in this - there are people who want to help.",
    "These feelings are temporary, even though they feel overwhelming right now.",
    "You've reached out for help, which shows incredible strength.",
    "There are people trained specifically to help in situations like this.",
    "Your life has value and meaning, even when it doesn't feel that way."
]

# Safety planning components
SAFETY_PLANNING_ELEMENTS = {
    "warning_signs": "Recognizing thoughts, feelings, and situations that might lead to crisis",
    "coping_strategies": "Things you can do on your own to help yourself feel better",
    "social_contacts": "People and social settings that provide distraction and support",
    "professional_contacts": "Mental health professionals and agencies to contact during crisis",
    "environment_safety": "Making your environment safer by removing or restricting access to lethal means",
    "reasons_for_living": "Things that are important to you and worth living for"
}
