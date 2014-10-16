__author__ = 'vti'

from datamodel import conn, cur

class Task:
    def __init__(self, task_id):
        self.id = task_id
        self.name = cur.execute('SELECT name FROM task WHERE id=?', (self.id,)).fetchone()[0]

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def edit(self, task_name):
        cur.execute('UPDATE task SET name = ? WHERE id =?', (task_name, self.id))
        conn.commit()

    def delete(self):
        cur.execute('DELETE FROM task WHERE id=?', (self.id,))
        conn.commit()