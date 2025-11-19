# utils/crisis_detection.py

import re
import streamlit as st  # type: ignore
from utils.gemini_client import GeminiClient
from utils.crisis_keywords import CRISIS_KEYWORDS, SEVERITY_WEIGHTS

# Map between different naming conventions to canonical levels
_CANON_LEVELS = {
    "low": "LOW",
    "moderate": "MODERATE",
    "high": "HIGH",
    "critical": "CRITICAL",
    "severe": "CRITICAL",
    "SEVERE": "CRITICAL",
    "LOW": "LOW",
    "MODERATE": "MODERATE",
    "HIGH": "HIGH"
}

class CrisisDetector:
    def __init__(self):
        try:
            # prefer session gemini client if present
            self.gemini_client = st.session_state.get('gemini_client') or GeminiClient()
        except Exception:
            self.gemini_client = None

        self.crisis_keywords = CRISIS_KEYWORDS
        self.severity_weights = SEVERITY_WEIGHTS
        
    def analyze_text_for_crisis(self, text):
        keyword_risk = self._keyword_based_detection(text)
        if self.gemini_client:
            try:
                ai_analysis = self.gemini_client.analyze_text_for_crisis(text)
            except Exception:
                ai_analysis = {"risk_level": "MODERATE", "keywords_detected": [], "analysis": "AI error"}
        else:
            ai_analysis = {"risk_level": "LOW", "keywords_detected": [], "analysis": "AI client unavailable."}
        
        combined = self._combine_risk_assessments(keyword_risk, ai_analysis)
        return combined
    
    def _keyword_based_detection(self, text):
        text_lower = text.lower()
        detected_keywords = []
        total_score = 0
        
        for category, keywords in self.crisis_keywords.items():
            for keyword in keywords:
                if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower):
                    detected_keywords.append((keyword, category))
                    total_score += self.severity_weights.get(category, 1)
        
        # Map score to canonical levels
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
        # canonical ordering
        order = ["low", "moderate", "high", "critical"]
        # ai risk -> normalize to lowercase/canonical
        raw_ai = ai_analysis.get("risk_level", "LOW")
        ai_level = _CANON_LEVELS.get(str(raw_ai).lower(), _CANON_LEVELS.get(str(raw_ai), "LOW")).lower()
        try:
            a_idx = order.index(ai_level)
        except ValueError:
            a_idx = 0
        try:
            k_idx = order.index(keyword_risk.get("risk_level", "low"))
        except ValueError:
            k_idx = 0
        combined_level = order[max(a_idx, k_idx)]
        # escalate if either says critical/severe
        if keyword_risk.get("risk_level") == "critical" or str(raw_ai).lower() in ("critical", "severe"):
            combined_level = "critical"
        return {
            "final_risk_level": combined_level,
            "keyword_analysis": keyword_risk,
            "ai_analysis": ai_analysis,
            "requires_intervention": combined_level in ["high", "critical"],
            "immediate_crisis": combined_level == "critical"
        }
    
    def trigger_crisis_intervention(self, risk_assessment):
        if risk_assessment.get("immediate_crisis"):
            self._show_immediate_crisis_resources()
        elif risk_assessment.get("requires_intervention"):
            self._show_support_resources()
        return risk_assessment.get("requires_intervention", False)
    
    def _show_immediate_crisis_resources(self):
        st.error("🚨 IMMEDIATE CRISIS RESOURCES — If you're in immediate danger call emergency services.")
        # guard data_manager
        if st.session_state.get('data_manager'):
            try:
                st.session_state.data_manager.log_crisis_event("immediate")
            except Exception:
                pass
    
    def _show_support_resources(self):
        st.warning("💛 We're here to support you — consider contacting local support or using coping strategies.")
        if st.session_state.get('data_manager'):
            try:
                st.session_state.data_manager.log_crisis_event("support")
            except Exception:
                pass
    
    def get_crisis_follow_up_message(self, risk_level):
        if risk_level in ("critical", "CRITICAL"):
            return "I'm really concerned about you right now. Please reach out to crisis resources. Would you like grounding exercises?"
        if risk_level in ("high", "HIGH"):
            return "I hear you're struggling — would you like to try some coping strategies together?"
        if risk_level in ("moderate", "MODERATE"):
            return "Thanks for sharing. Would you like to work through coping techniques?"
        return "Thank you for sharing. I'm here to listen. What would be most helpful for you?"
