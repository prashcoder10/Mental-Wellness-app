# utils/crisis_detection.py

import re
import streamlit as st # type: ignore
from utils.gemini_client import GeminiClient # 🌟 CHANGE: Import the new GeminiClient
from data.crisis_keywords import CRISIS_KEYWORDS, SEVERITY_WEIGHTS

class CrisisDetector:
    def __init__(self):
        # 🌟 CHANGE: Initialize the GeminiClient
        # Note: In the Streamlit flow, this client should already be initialized
        # via st.session_state.gemini_client, but we'll instantiate one here
        # to ensure the method call works, or we will modify the calling component.
        # Since this class is instantiated in chat_interface.py, we rely on the
        # calling context, but for a standalone fix, we'll try to use the client.
        try:
            self.gemini_client = GeminiClient()
        except Exception:
            # Fallback if the client can't be created here
            self.gemini_client = None 

        self.crisis_keywords = CRISIS_KEYWORDS
        self.severity_weights = SEVERITY_WEIGHTS
        
    def analyze_text_for_crisis(self, text):
        """Multi-layered crisis detection system"""
        
        # Layer 1: Keyword-based detection
        keyword_risk = self._keyword_based_detection(text)
        
        # Layer 2: AI-powered sentiment and risk analysis (using Gemini)
        if self.gemini_client:
            # 🌟 CHANGE: Use the GeminiClient's dedicated crisis analysis method
            ai_analysis = self.gemini_client.analyze_text_for_crisis(text)
        else:
            # Fallback if client initialization failed
            ai_analysis = {"risk_level": "LOW", "keywords_detected": [], "analysis": "AI client unavailable."}
        
        # Layer 3: Combined risk assessment
        combined_risk = self._combine_risk_assessments(keyword_risk, ai_analysis)
        
        return combined_risk
    
    def _keyword_based_detection(self, text):
        """Detect crisis keywords and calculate risk score"""
        text_lower = text.lower()
        detected_keywords = []
        total_score = 0
        
        for category, keywords in self.crisis_keywords.items():
            for keyword in keywords:
                if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower):
                    detected_keywords.append((keyword, category))
                    total_score += self.severity_weights.get(category, 1)
        
        # Determine risk level based on score
        if total_score >= 10:
            risk_level = "critical"
        elif total_score >= 6:
            risk_level = "high"
        elif total_score >= 3:
            risk_level = "moderate"
        else:
            risk_level = "low"
        
        return {
            "risk_level": risk_level,
            "score": total_score,
            "detected_keywords": detected_keywords,
            "method": "keyword_analysis"
        }
    
    def _combine_risk_assessments(self, keyword_risk, ai_analysis):
        """Combine multiple risk assessment methods"""
        
        # Risk level hierarchy: critical > high > moderate > low
        risk_levels = ["low", "moderate", "high", "critical"]
        
        # Safely get index, defaulting to low if risk_level is unexpected
        try:
            keyword_level_idx = risk_levels.index(keyword_risk["risk_level"])
        except ValueError:
            keyword_level_idx = risk_levels.index("low")
            
        try:
            ai_level_idx = risk_levels.index(ai_analysis["risk_level"].lower()) # Ensure lowercase from AI
        except ValueError:
            ai_level_idx = risk_levels.index("low")
        
        # Take the higher risk level
        combined_level = risk_levels[max(keyword_level_idx, ai_level_idx)]
        
        # If either method detects critical risk, escalate immediately
        if keyword_risk["risk_level"] == "critical" or ai_analysis["risk_level"].lower() == "critical":
            combined_level = "critical"
        
        return {
            "final_risk_level": combined_level,
            "keyword_analysis": keyword_risk,
            "ai_analysis": ai_analysis,
            "requires_intervention": combined_level in ["high", "critical"],
            "immediate_crisis": combined_level == "critical"
        }
    
    def trigger_crisis_intervention(self, risk_assessment):
        """Display appropriate crisis intervention based on risk level"""
        
        if risk_assessment["immediate_crisis"]:
            self._show_immediate_crisis_resources()
        elif risk_assessment["requires_intervention"]:
            self._show_support_resources()
            
        return risk_assessment["requires_intervention"]
    
    def _show_immediate_crisis_resources(self):
        """Display immediate crisis intervention resources"""
        st.error("""
        🚨 **IMMEDIATE CRISIS RESOURCES**
        
        **If you're in immediate danger, call 911**
        
        **For mental health crisis support:**
        - 🆘 **Call 988** - Suicide & Crisis Lifeline (24/7)
        - 💬 **Text HOME to 741741** - Crisis Text Line
        - 🌐 **Chat online**: [suicidepreventionlifeline.org](https://suicidepreventionlifeline.org)
        
        **Remember:** You matter, and there are people who want to help. These services are free, confidential, and available 24/7.
        """)
        
        # Log crisis event (anonymized)
        st.session_state.data_manager.log_crisis_event("immediate")
    
    def _show_support_resources(self):
        """Display general support resources"""
        st.warning("""
        💛 **We're here to support you**
        
        It sounds like you might be going through a tough time. Here are some resources that can help:
        
        **Talk to someone:**
        - 📞 **988** - Suicide & Crisis Lifeline
        - 💬 **Text HOME to 741741** - Crisis Text Line
        - 🏥 **Find local mental health services**: [samhsa.gov/find-help](https://www.samhsa.gov/find-help)
        
        **Immediate coping strategies:**
        - Take 5 deep breaths
        - Name 5 things you can see, 4 you can touch, 3 you can hear
        - Reach out to a trusted friend or family member
        - Use our breathing exercises tool
        
        Remember: Seeking help is a sign of strength, not weakness.
        """)
        
        # Log support event (anonymized)
        st.session_state.data_manager.log_crisis_event("support")
    
    def get_crisis_follow_up_message(self, risk_level):
        """Generate appropriate follow-up message after crisis detection"""
        
        if risk_level == "critical":
            return """
            I'm really concerned about you right now. Please reach out to one of the crisis resources above. 
            You don't have to go through this alone, and there are people trained to help in situations like this.
            
            Would you like to try some grounding exercises while you consider reaching out for help?
            """
        
        elif risk_level == "high":
            return """
            I can hear that you're struggling right now, and I want you to know that your feelings are valid. 
            It might be helpful to talk to someone who can provide more support than I can offer.
            
            In the meantime, would you like to explore some coping strategies together?
            """
        
        elif risk_level == "moderate":
            return """
            It sounds like you're dealing with some difficult feelings. That takes courage to share.
            
            Would you like to work through some coping techniques, or would you prefer to talk about 
            what's been on your mind?
            """
        
        return """
        Thank you for sharing. I'm here to listen and support you. 
        What would be most helpful for you right now?
        """
