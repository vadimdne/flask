__author__ = 'vti'
import hashlib
import uuid
import time
from datamodel import cur
from models.tasklist import Tasklist

SESSION_DURATION = 5


class User:
    def __init__(self, username):
        self.username = username
        self.id = cur.execute('SELECT id FROM user WHERE username=?', (self.username,)).fetchone()[0]
        self.session_id = self.create_session()

    def create_session(self):
        session_id = uuid.uuid4().hex
        start_time = time.time()
        end_time = start_time + SESSION_DURATION
        cur.execute(
            'INSERT INTO session(id, start_time, end_time, user_id) VALUES (?, ?, ?, ?)',
            (session_id, start_time, end_time, self.id)
        )
        return session_id

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

    def verify_password(self, password_attempt):
        salt = cur.execute('SELECT salt FROM user WHERE id=?', (self.id,)).fetchone()[0]
        hashed = cur.execute('SELECT hash FROM user WHERE id=?', (self.id,)).fetchone()[0]
        if hashlib.sha512(salt+password_attempt).hexdigest() == hashed:
            return True
        else:
            return False

    def get_tasklists(self):
        tasklists = []
        for tasklist_id in cur.execute('SELECT id FROM tasklist WHERE user_id=?', (self.id,)).fetchall():
            tasklists.append(Tasklist(tasklist_id[0]))
        return tasklists

    def add_tasklist(self, tasklist_name):
        cur.execute('INSERT INTO tasklist (name, user_id) VALUES (?,?)', (tasklist_name, self.id))
