class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, session_id, user_data):
        if session_id not in self.sessions:
            self.sessions[session_id] = user_data
            return True
        return False

    def get_session(self, session_id):
        return self.sessions.get(session_id)

    def update_session(self, session_id, user_data):
        if session_id in self.sessions:
            self.sessions[session_id] = user_data
            return True
        return False

    def delete_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]
            return True
        return False

    def list_sessions(self):
        return list(self.sessions.keys())

# Misol
session_manager = SessionManager()

# Session yaratish
session_manager.create_session("session1", {"user_id": 1, "username": "john"})

# Session olish
print(session_manager.get_session("session1"))  # {"user_id": 1, "username": "john"}

# Session yangilash
session_manager.update_session("session1", {"user_id": 1, "username": "jane"})

# Session olish
print(session_manager.get_session("session1"))  # {"user_id": 1, "username": "jane"}

# Session o'chirish
session_manager.delete_session("session1")

# Sessionlar ro'yxati
print(session_manager.list_sessions())  # []
