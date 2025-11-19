import json
import streamlit as st # type: ignore
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
import base64
import os

class DataManager:
    def __init__(self, user_id):
        self.user_id = user_id
        self.encryption_key = self._get_or_create_encryption_key()
        self.fernet = Fernet(self.encryption_key)
        
        # Initialize session state data structures
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        if 'mood_entries' not in st.session_state:
            st.session_state.mood_entries = []
        if 'journal_entries' not in st.session_state:
            st.session_state.journal_entries = []
        if 'cbt_records' not in st.session_state:
            st.session_state.cbt_records = []
        if 'crisis_events' not in st.session_state:
            st.session_state.crisis_events = []
    
    def _get_or_create_encryption_key(self):
        """Generate or retrieve encryption key for this session"""
        if 'encryption_key' not in st.session_state:
            st.session_state.encryption_key = Fernet.generate_key()
        return st.session_state.encryption_key
    
    def encrypt_data(self, data):
        """Encrypt sensitive data"""
        json_data = json.dumps(data).encode()
        encrypted_data = self.fernet.encrypt(json_data)
        return base64.b64encode(encrypted_data).decode()
    
    def decrypt_data(self, encrypted_data):
        """Decrypt sensitive data"""
        try:
            encrypted_bytes = base64.b64decode(encrypted_data.encode())
            decrypted_data = self.fernet.decrypt(encrypted_bytes)
            return json.loads(decrypted_data.decode())
        except:
            return None
    
    def save_chat_message(self, role, content, persona=None, risk_level=None):
        """Save chat message with optional metadata"""
        message = {
            "id": len(st.session_state.chat_history),
            "timestamp": datetime.now().isoformat(),
            "role": role,
            "content": content,
            "persona": persona,
            "risk_level": risk_level
        }
        st.session_state.chat_history.append(message)
    
    def save_mood_entry(self, mood_data):
        """Save mood tracking data"""
        entry = {
            "id": len(st.session_state.mood_entries),
            "timestamp": datetime.now().isoformat(),
            "overall_mood": mood_data.get("overall_mood"),
            "emotions": mood_data.get("emotions", []),
            "intensity": mood_data.get("intensity"),
            "triggers": mood_data.get("triggers", []),
            "notes": mood_data.get("notes", "")
        }
        st.session_state.mood_entries.append(entry)
    
    def save_journal_entry(self, entry_data):
        """Save journal entry"""
        entry = {
            "id": len(st.session_state.journal_entries),
            "timestamp": datetime.now().isoformat(),
            "prompt": entry_data.get("prompt"),
            "content": entry_data.get("content"),
            "focus_area": entry_data.get("focus_area"),
            "mood_before": entry_data.get("mood_before"),
            "mood_after": entry_data.get("mood_after"),
            "insights": entry_data.get("insights", [])
        }
        st.session_state.journal_entries.append(entry)
    
    def save_cbt_record(self, cbt_data):
        """Save CBT thought record"""
        record = {
            "id": len(st.session_state.cbt_records),
            "timestamp": datetime.now().isoformat(),
            "situation": cbt_data.get("situation"),
            "thoughts": cbt_data.get("thoughts"),
            "emotions": cbt_data.get("emotions"),
            "intensity_before": cbt_data.get("intensity_before"),
            "evidence_for": cbt_data.get("evidence_for"),
            "evidence_against": cbt_data.get("evidence_against"),
            "balanced_thought": cbt_data.get("balanced_thought"),
            "intensity_after": cbt_data.get("intensity_after"),
            "ai_insights": cbt_data.get("ai_insights")
        }
        st.session_state.cbt_records.append(record)
    
    def log_crisis_event(self, crisis_type):
        """Log crisis intervention event (anonymized)"""
        event = {
            "id": len(st.session_state.crisis_events),
            "timestamp": datetime.now().isoformat(),
            "type": crisis_type,  # "immediate", "support", "resolved"
            "session_id": self.user_id[:8]  # Truncated for privacy
        }
        st.session_state.crisis_events.append(event)
    
    def get_recent_mood_data(self, days=7):
        """Get mood data from recent days"""
        cutoff_date = datetime.now() - timedelta(days=days)
        recent_entries = []
        
        for entry in st.session_state.mood_entries:
            entry_date = datetime.fromisoformat(entry["timestamp"])
            if entry_date >= cutoff_date:
                recent_entries.append(entry)
        
        return recent_entries
    
    def get_mood_trends(self):
        """Analyze mood trends for visualization"""
        if not st.session_state.mood_entries:
            return {"dates": [], "moods": [], "average": 5}
        
        dates = []
        moods = []
        
        for entry in st.session_state.mood_entries[-30:]:  # Last 30 entries
            dates.append(datetime.fromisoformat(entry["timestamp"]).date())
            moods.append(entry["overall_mood"])
        
        average_mood = sum(moods) / len(moods) if moods else 5
        
        return {
            "dates": dates,
            "moods": moods,
            "average": round(average_mood, 1)
        }
    
    def get_journal_themes(self):
        """Extract common themes from journal entries"""
        if not st.session_state.journal_entries:
            return []
        
        themes = {}
        for entry in st.session_state.journal_entries:
            focus_area = entry.get("focus_area", "general")
            themes[focus_area] = themes.get(focus_area, 0) + 1
        
        return sorted(themes.items(), key=lambda x: x[1], reverse=True)
    
    def get_data_summary(self):
        """Get summary of all user data for privacy dashboard"""
        return {
            "session_id": self.user_id[:8] + "...",
            "session_duration": str(datetime.now() - st.session_state.session_start),
            "total_chat_messages": len(st.session_state.chat_history),
            "mood_entries": len(st.session_state.mood_entries),
            "journal_entries": len(st.session_state.journal_entries),
            "cbt_records": len(st.session_state.cbt_records),
            "crisis_events": len(st.session_state.crisis_events),
            "last_activity": datetime.now().isoformat()
        }
    
    def export_user_data(self):
        """Export all user data in JSON format"""
        export_data = {
            "export_timestamp": datetime.now().isoformat(),
            "session_summary": self.get_data_summary(),
            "mood_entries": st.session_state.mood_entries,
            "journal_entries": st.session_state.journal_entries,
            "cbt_records": st.session_state.cbt_records,
            "data_notice": "This export contains your wellness data from this anonymous session. No personal identifiers are included."
        }
        
        return json.dumps(export_data, indent=2)
    
    def delete_all_data(self):
        """Securely delete all user data"""
        st.session_state.chat_history = []
        st.session_state.mood_entries = []
        st.session_state.journal_entries = []
        st.session_state.cbt_records = []
        st.session_state.crisis_events = []
        
        # Generate new encryption key
        st.session_state.encryption_key = Fernet.generate_key()
        self.fernet = Fernet(st.session_state.encryption_key)
    
    def get_conversation_history(self, limit=10):
        """Get recent conversation history for AI context"""
        recent_messages = st.session_state.chat_history[-limit:]
        conversation = []
        
        for msg in recent_messages:
            conversation.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        
        return conversation
