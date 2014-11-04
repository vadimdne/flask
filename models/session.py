__author__ = 'vti'
from datamodel import cur
import uuid
import time

SESSION_DURATION = 5


class Session:
    def __init__(self, user_id):
        self.id = uuid.uuid4().hex
        self.start_time = time.time()
        self.end_time = self.start_time + SESSION_DURATION
        cur.execute(
            'INSERT INTO session(id, start_time, end_time, user_id) VALUES (?, ?, ?, ?)',
            (self.id, self.start_time, self.end_time, user_id)
        )

    @staticmethod
    def verify_session(session_id):
        if not session_id:
            return False
        current_time = time.time()
        end_time = cur.execute('SELECT end_time FROM session WHERE id=?', (session_id,)).fetchone()[0]
        if current_time > end_time:
            return False
        return True

    @staticmethod
    def refresh_session(session_id):
        end_time = time.time() + SESSION_DURATION
        cur.execute('UPDATE session SET end_time = ? WHERE id =?', (end_time, session_id))

    @staticmethod
    def drop_session(session_id):
        end_time = time.time()
        cur.execute('UPDATE session SET end_time = ? WHERE id =?', (end_time, session_id))