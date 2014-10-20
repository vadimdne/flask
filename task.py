__author__ = 'vti'

from datamodel import conn, cur

class Task:
    def __init__(self, task_id):
        self.id = task_id
        self.name = cur.execute('SELECT name FROM task WHERE id=?', (self.id,)).fetchone()[0]

    def edit(self, task_name):
        cur.execute('UPDATE task SET name = ? WHERE id =?', (task_name, self.id))

    def delete(self):
        cur.execute('DELETE FROM task WHERE id=?', (self.id,))