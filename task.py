__author__ = 'vti'

from datamodel import cur

class Task:
    def __init__(self, task_id):
        self.id = task_id
        self.name = cur.execute('SELECT name FROM task WHERE id=?', (self.id,)).fetchone()[0]

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name