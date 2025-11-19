# utils/data_manager.py

import json
import streamlit as st  # type: ignore
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
import base64
import os
import uuid

class DataManager:
    def __init__(self, user_id=None):
        # allow None and generate anonymous id
        if user_id is None:
            user_id = str(uuid.uuid4())
        self.user_id = user_id
        self.encryption_key = self._get_or_create_encryption_key()
        self.fernet = Fernet(self.encryption_key)
        
        # Initialize session state data structures defensively
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
        if 'session_start' not in st.session_state:
            st.session_state.session_start = datetime.now().isoformat()
    
    def _get_or_create_encryption_key(self):
        if 'encryption_key' not in st.session_state:
            st.session_state.encryption_key = Fernet.generate_key()
        return st.session_state.encryption_key
    
    def encrypt_data(self, data):
        json_data = json.dumps(data).encode()
        encrypted_data = self.fernet.encrypt(json_data)
        return base64.b64encode(encrypted_data).decode()
    
    def decrypt_data(self, encrypted_data):
        try:
            encrypted_bytes = base64.b64decode(encrypted_data.encode())
            decrypted_data = self.fernet.decrypt(encrypted_bytes)
            return json.loads(decrypted_data.decode())
        except Exception:
            return None
    
    def save_chat_message(self, role, content, persona=None, risk_level=None):
        message = {
            "id": len(st.session_state.chat_history),
            "timestamp": datetime.now().isoformat(),
            "role": role,
            "content": content,
            "persona": persona,
            "risk_level": risk_level
        }
        st.session_state.chat_history.append(message)
    
    # other methods unchanged but left as-is (they rely on the session keys we ensure above)

    def get_conversation_history(self, limit=10):
        recent_messages = st.session_state.chat_history[-limit:]
        conversation = []
        for msg in recent_messages:
            conversation.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        return conversation
