__author__ = 'vti'

from datamodel import conn, cur
from task import Task

class Tasklist:
    def __init__(self, tasklist_id):
        self.id = tasklist_id
        self.name = cur.execute('SELECT name FROM tasklist WHERE id=?', (self.id,)).fetchone()[0]

    def edit(self, tasklist_name):
        cur.execute('UPDATE tasklist SET name = ? WHERE id =?', (tasklist_name, self.id))

    def delete(self):
        cur.execute('DELETE FROM tasklist WHERE id=?', (self.id,))

    def get_tasks(self):
        tasks = []
        for task_id in cur.execute('SELECT id FROM task WHERE tasklist_id=?', (self.id,)).fetchall():
            tasks.append(Task(task_id[0]))
        return tasks

    def add_task(self, task_name):
        cur.execute('INSERT INTO task (name, tasklist_id) VALUES (?,?)', (task_name, self.id))


