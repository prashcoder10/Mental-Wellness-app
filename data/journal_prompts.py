"""
Structured journal prompts organized by focus areas and therapeutic approaches
Based on CBT principles and evidence-based journaling techniques
"""

# Core journal prompts organized by therapeutic focus areas
JOURNAL_PROMPTS = {
    "emotional_awareness": [
        "What emotions have you experienced today? How did each one feel in your body?",
        "Describe a moment when you felt a strong emotion. What triggered it?",
        "What emotion do you find most difficult to experience? Why might that be?",
        "How do you typically express different emotions? Which ways feel healthiest?",
        "What would you say to comfort yourself when you're feeling your most difficult emotion?",
        "Describe a time when you felt truly understood by someone. What did that feel like?",
        "What emotions do you notice most often? What might they be telling you?",
        "How has your relationship with your emotions changed over time?",
        "What would it look like to be more compassionate toward your feelings?",
        "If your emotions could speak, what would they want you to know?"
    ],
    
    "thought_patterns": [
        "What thoughts have been on repeat in your mind lately?",
        "Describe a situation where your first thought turned out to be wrong. What did you learn?",
        "What negative thought about yourself comes up most often? What evidence challenges it?",
        "How do your thoughts change when you're in different moods?",
        "What thought patterns do you notice when you're stressed versus when you're calm?",
        "If you could change one recurring negative thought, what would it be?",
        "What assumptions do you make about what others think of you? How accurate are they?",
        "Describe a time when changing your perspective completely changed your experience.",
        "What would you think about this situation if it happened to your best friend?",
        "What thoughts help you feel confident and capable?"
    ],
    
    "gratitude": [
        "What are three things you're grateful for today, and why?",
        "Describe someone who has positively impacted your life. What did they do?",
        "What challenges in your life have ultimately led to growth or positive changes?",
        "What abilities or skills do you have that you're thankful for?",
        "What small, everyday pleasures bring you joy?",
        "What opportunities do you have that you sometimes take for granted?",
        "What about your past has contributed to who you are today in positive ways?",
        "What aspects of your current situation are actually going well?",
        "What kindness have you witnessed or experienced recently?",
        "If you could only keep five things in your life, what would they be and why?"
    ],
    
    "coping_skills": [
        "What strategies help you feel better when you're upset? Which ones actually work?",
        "Describe a time you successfully handled a difficult situation. What did you do?",
        "What are your warning signs that stress is building up? How can you respond early?",
        "What activities make you feel grounded and centered?",
        "How do you typically ask for help? What makes it easier or harder?",
        "What would your ideal self-care routine look like?",
        "What boundaries do you need to set to protect your mental health?",
        "Describe a time when you surprised yourself with your resilience.",
        "What environments or situations help you feel most like yourself?",
        "What would you want to remember when you're going through a tough time?"
    ],
    
    "goals": [
        "What do you want to accomplish in the next month? Why is this important to you?",
        "What's one small step you could take today toward a larger goal?",
        "What obstacles typically get in the way of your goals? How might you address them?",
        "What would you attempt if you knew you couldn't fail?",
        "What skills would you like to develop? What draws you to them?",
        "How do you define success for yourself, separate from others' expectations?",
        "What goals have you achieved in the past? What helped you succeed?",
        "What would you like your life to look like in five years?",
        "What small changes could you make to move closer to the person you want to be?",
        "What values do you want your goals to reflect?"
    ],
    
    "relationships": [
        "What qualities do you value most in your friendships?",
        "Describe a relationship that brings out the best in you. What makes it special?",
        "How do you typically handle conflict? What would you like to change?",
        "What do you wish people understood about you?",
        "How do you show care for the people important to you?",
        "What boundaries are important to you in relationships?",
        "Describe a time when someone's support made a real difference for you.",
        "What role do you usually play in your friend group or family? How do you feel about it?",
        "How has your relationship with yourself changed over time?",
        "What would you like to improve about how you communicate with others?"
    ],
    
    "daily_reflection": [
        "What went well today? What was challenging?",
        "What did you learn about yourself today?",
        "How did you take care of yourself today?",
        "What moment from today would you want to remember?",
        "What would you do differently if you could replay today?",
        "How did you connect with others today?",
        "What emotions did you experience today? What triggered them?",
        "What are you looking forward to tomorrow?",
        "What progress did you make toward your goals today?",
        "What are you proud of from today, no matter how small?"
    ]
}

# CBT-specific journal prompts for therapeutic insight
CBT_PROMPTS = {
    "emotional_awareness": [
        "Rate your emotions today from 1-10 and describe what influenced these ratings.",
        "What physical sensations did you notice when experiencing different emotions today?",
        "How did your emotions influence your behavior today?",
        "What would happen if you allowed yourself to fully feel your emotions without judging them?",
        "What emotions are you most comfortable with? Which ones do you try to avoid?"
    ],
    
    "thought_patterns": [
        "Identify three thoughts that caused you distress today. What cognitive distortions might be present?",
        "What evidence supports your worries? What evidence contradicts them?",
        "How would you challenge your most persistent negative thought?",
        "What would you tell a friend who had the same negative thoughts you're having?",
        "Track one negative thought pattern for a week. What patterns do you notice?"
    ],
    
    "behavioral_patterns": [
        "What behaviors helped your mood today? Which ones made it worse?",
        "What activities did you avoid today? What thoughts or feelings led to avoidance?",
        "How did your behavior align with your values today?",
        "What would you do differently today if fear wasn't a factor?",
        "What small behavioral changes could improve your well-being?"
    ],
    
    "problem_solving": [
        "What problem are you currently facing? List all possible solutions, even unrealistic ones.",
        "Break down a current challenge into smaller, manageable steps.",
        "What has worked for similar problems in the past?",
        "What advice would you give someone else facing this same problem?",
        "What would the ideal outcome look like? What steps could move you toward it?"
    ],
    
    "cognitive_restructuring": [
        "Rewrite a negative thought about yourself in a more balanced way.",
        "What assumptions are you making in a current situation? How could you test these assumptions?",
        "What would a neutral observer say about your situation?",
        "How might you view this situation in 5 years?",
        "What facts are you focusing on versus what interpretations are you adding?"
    ]
}

# Therapeutic writing prompts for specific challenges
THERAPEUTIC_PROMPTS = {
    "anxiety": [
        "What are your worries telling you they're trying to protect you from?",
        "Describe a time you thought something terrible would happen, but it didn't.",
        "What would you do today if anxiety wasn't holding you back?",
        "Write a letter to your anxiety. What would you want it to know?",
        "What steps could you take to prepare for situations that make you anxious?"
    ],
    
    "depression": [
        "What activities used to bring you joy? What made them meaningful?",
        "Write about a time when you felt proud of yourself.",
        "What would you tell someone you love who was feeling the way you feel now?",
        "What small thing could you do today to take care of yourself?",
        "What hopes do you have for your future, even if they feel distant right now?"
    ],
    
    "low_self_esteem": [
        "List 10 things you like about yourself, including small things.",
        "What would your best friend say are your greatest strengths?",
        "Describe a time when you handled a difficult situation well.",
        "What accomplishments are you proud of, big or small?",
        "What qualities do you admire in yourself that you'd want in a friend?"
    ],
    
    "stress": [
        "What aspects of your current stress are within your control? Which aren't?",
        "How does stress show up in your body? What helps you release it?",
        "What would a typical day look like if you had less stress?",
        "What boundaries could you set to reduce stress in your life?",
        "What stress management techniques have you tried? Which were most helpful?"
    ],
    
    "transitions": [
        "What are you leaving behind in this transition? What are you moving toward?",
        "What skills or strengths have helped you through changes before?",
        "What are you most excited about in this new phase of life?",
        "What fears do you have about this change? Which ones are realistic?",
        "How do you want to grow or change during this transition?"
    ]
}

# Weekly themed journal challenges
WEEKLY_THEMES = {
    "self_compassion_week": [
        "Day 1: How do you typically talk to yourself when you make mistakes?",
        "Day 2: Write yourself a compassionate letter about a recent struggle.",
        "Day 3: What would unconditional self-acceptance look like for you?",
        "Day 4: How would you comfort your younger self during a difficult time?",
        "Day 5: What are three ways you can be gentler with yourself?",
        "Day 6: What would change if you truly believed you were worthy of love?",
        "Day 7: Reflect on how practicing self-compassion has felt this week."
    ],
    
    "growth_mindset_week": [
        "Day 1: What challenges are you currently facing that could lead to growth?",
        "Day 2: Describe a time when failure led to something positive.",
        "Day 3: What skills would you like to develop? Why do they interest you?",
        "Day 4: How has a past struggle made you stronger or wiser?",
        "Day 5: What would you try if you embraced the possibility of failure?",
        "Day 6: How can you view your current challenges as opportunities?",
        "Day 7: What have you learned about growth and resilience this week?"
    ],
    
    "gratitude_week": [
        "Day 1: What are you grateful for in your living situation?",
        "Day 2: What relationships are you thankful for and why?",
        "Day 3: What opportunities do you have that you appreciate?",
        "Day 4: What challenges have led to positive growth?",
        "Day 5: What abilities or talents are you grateful to have?",
        "Day 6: What simple pleasures bring you joy?",
        "Day 7: How has focusing on gratitude affected your mood this week?"
    ],
    
    "values_exploration_week": [
        "Day 1: What activities make you feel most like yourself?",
        "Day 2: What causes or issues do you care deeply about?",
        "Day 3: What kind of person do you want to be in relationships?",
        "Day 4: What principles guide your important decisions?",
        "Day 5: How do you want to contribute to the world?",
        "Day 6: What would you do if you had unlimited resources?",
        "Day 7: How can you align your daily life more closely with your values?"
    ]
}

# Mindfulness-based journal prompts
MINDFULNESS_PROMPTS = [
    "Describe this present moment using all five senses. What do you notice?",
    "What thoughts are passing through your mind right now? Can you observe them without attachment?",
    "How is your body feeling right now? What sensations are you aware of?",
    "What emotions are present for you in this moment? How do they feel in your body?",
    "What are you grateful for in this exact moment?",
    "If you could send a message to your past self from a year ago, what would you say?",
    "What is your breath telling you about how you're feeling right now?",
    "Describe the space around you as if you're seeing it for the first time.",
    "What judgments are you carrying about yourself today? Can you let them go?",
    "How can you be more present in your daily activities?"
]

# Creativity and expression prompts
CREATIVE_PROMPTS = [
    "If your life was a story, what chapter are you in now? What do you hope happens next?",
    "Describe yourself as if you were a character in a book. What are your strengths and quirks?",
    "What would your life look like if it was a movie? What genre would it be?",
    "Write a letter to yourself from 10 years in the future. What wisdom would future you share?",
    "If you could have a conversation with any version of yourself, which would you choose and why?",
    "Describe your ideal day from start to finish. What would make it perfect?",
    "What would you create if you had unlimited artistic ability?",
    "Write about a place where you feel completely at peace. What makes it special?",
    "If you could give your younger self one piece of advice, what would it be?",
    "What metaphor best describes your current life situation?"
]

# Quick daily check-in prompts (for busy days)
QUICK_PROMPTS = [
    "Three words to describe your day:",
    "One thing that went well today:",
    "One thing you're grateful for:",
    "How are you feeling right now?",
    "What do you need most today?",
    "One thing you learned today:",
    "How did you take care of yourself today?",
    "What are you looking forward to?",
    "What challenged you today?",
    "One positive thing about yourself:"
]

# Seasonal and contextual prompts
SEASONAL_PROMPTS = {
    "new_year": [
        "What do you want to leave behind from last year?",
        "What hopes do you have for the year ahead?",
        "What kind of person do you want to become this year?",
        "What habits would you like to develop?",
        "How do you want to grow in the coming year?"
    ],
    
    "back_to_school": [
        "What are you most excited about for the new school year?",
        "What goals do you have for your academic life?",
        "How do you want to approach challenges this year?",
        "What kind of student do you want to be?",
        "What support do you need to succeed?"
    ],
    
    "difficult_times": [
        "What is helping you get through this difficult time?",
        "What strengths are you discovering in yourself?",
        "Who or what are you most grateful for right now?",
        "What gives you hope, even in small ways?",
        "How are you taking care of yourself during this time?"
    ]
}
