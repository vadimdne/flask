__author__ = 'vti'
from datamodel import cur
from tasklist import Tasklist

class User:
    def __init__(self, username):
        self.username = username
        self.id = cur.execute('SELECT id FROM user WHERE username=?', (self.username,)).fetchone()[0]

    def get_password(self):
        return cur.execute('SELECT password FROM user WHERE id=?', (self.id,)).fetchone()[0]

    def get_first_tasklist(self):
        tasklist_id = cur.execute('SELECT id FROM tasklist WHERE user_id=?', (self.id,)).fetchone()[0]
        return Tasklist(tasklist_id)

    def get_tasklists(self):
        tasklists = []
        for tasklist_id in cur.execute('SELECT id FROM tasklist WHERE user_id=?', (self.id,)).fetchall():
            tasklists.append(Tasklist(tasklist_id[0]))
        return tasklists

    def add_tasklist(self, tasklist_name):
        cur.execute('INSERT INTO tasklist (name, user_id) VALUES (?,?)', (tasklist_name, self.id))
