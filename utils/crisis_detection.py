import re
import streamlit as st
from utils.gemini_client import GeminiClient
from data.crisis_keywords import CRISIS_KEYWORDS, SEVERITY_WEIGHTS


_CANON_LEVELS = {
    "low": "LOW",
    "moderate": "MODERATE",
    "high": "HIGH",
    "critical": "CRITICAL",
    "severe": "CRITICAL",
    "LOW": "LOW",
    "MODERATE": "MODERATE",
    "HIGH": "HIGH",
    "SEVERE": "CRITICAL"
}


class CrisisDetector:
    def __init__(self):
        try:
            self.gemini_client = st.session_state.get("gemini_client") or GeminiClient()
        except Exception:
            self.gemini_client = None

        self.crisis_keywords = CRISIS_KEYWORDS
        self.severity_weights = SEVERITY_WEIGHTS

    def analyze_text_for_crisis(self, text):
        keyword_risk = self._keyword_based_detection(text)

        ai_analysis = {
            "risk_level": "LOW",
            "keywords_detected": [],
            "analysis": "AI unavailable"
        }

        if self.gemini_client:
            try:
                result = self.gemini_client.analyze_text_for_crisis(text)
                if isinstance(result, dict):
                    ai_analysis = result
            except Exception:
                pass

        combined = self._combine_risk_assessments(keyword_risk, ai_analysis)
        return combined

    def _keyword_based_detection(self, text):
        text_lower = text.lower()
        detected_keywords = []
        total_score = 0

        for category, keywords in self.crisis_keywords.items():
            for keyword in keywords:
                if re.search(r"\b" + re.escape(keyword) + r"\b", text_lower):
                    detected_keywords.append((keyword, category))
                    total_score += self.severity_weights.get(category, 1)

        if total_score >= 10:
            level = "critical"
        elif total_score >= 6:
            level = "high"
        elif total_score >= 3:
            level = "moderate"
        else:
            level = "low"

        return {
            "risk_level": level,
            "score": total_score,
            "detected_keywords": detected_keywords,
            "method": "keyword_analysis"
        }

    def _combine_risk_assessments(self, keyword_risk, ai):
        order = ["low", "moderate", "high", "critical"]

        raw_ai = ai.get("risk_level", "LOW")
        ai_level = _CANON_LEVELS.get(str(raw_ai), "LOW").lower()

        try:
            ai_rank = order.index(ai_level)
        except:
            ai_rank = 0

        try:
            kw_rank = order.index(keyword_risk.get("risk_level", "low"))
        except:
            kw_rank = 0

        final_level = order[max(ai_rank, kw_rank)]

        if keyword_risk["risk_level"] == "critical" or raw_ai.lower() in ("critical", "severe"):
            final_level = "critical"

        return {
            "final_risk_level": final_level,
            "keyword_analysis": keyword_risk,
            "ai_analysis": ai,
            "requires_intervention": final_level in ["high", "critical"],
            "immediate_crisis": final_level == "critical"
        }

    def trigger_crisis_intervention(self, assessment):
        if assessment.get("immediate_crisis"):
            self._show_immediate_crisis_resources()
        elif assessment.get("requires_intervention"):
            self._show_support_resources()
        return assessment.get("requires_intervention", False)

    def _show_immediate_crisis_resources(self):
        st.error("🚨 IMMEDIATE CRISIS — please call emergency services.")
        if st.session_state.get("data_manager"):
            try:
                st.session_state.data_manager.log_crisis_event("immediate")
            except:
                pass

    def _show_support_resources(self):
        st.warning("💛 You're not alone — consider reaching out for support.")
        if st.session_state.get("data_manager"):
            try:
                st.session_state.data_manager.log_crisis_event("support")
            except:
                pass

    def get_crisis_follow_up_message(self, risk_level):
        level = risk_level.upper()
        if level == "CRITICAL":
            return "I'm really concerned — please reach out to crisis resources. Would grounding exercises help?"
        if level == "HIGH":
            return "I hear you're struggling — want to try coping techniques together?"
        if level == "MODERATE":
            return "Thanks for sharing. Would you like some support techniques?"
        return "I'm here for you. What would be most helpful?"
