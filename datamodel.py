__author__ = 'vti'
import sqlite3

DATABASE = "F:\\tasks.db"

conn = sqlite3.connect(DATABASE, check_same_thread=False)
conn.isolation_level = None
cur = conn.cursor()

if __name__ == "__main__":
    cur.executescript("""
    DROP TABLE IF EXISTS user;
    CREATE TABLE user(
      id INT PRIMARY KEY NOT NULL,
      username TEXT NOT NULL,
      password TEXT NOT NULL
    );

    INSERT INTO user (id, username, password) VALUES (1, 'vadim', 'vadim');
    INSERT INTO user (id, username, password) VALUES (2, 'roman', 'roman');
    INSERT INTO user (id, username, password) VALUES (3, 'igor', 'igor');

    DROP TABLE IF EXISTS tasklist;
    CREATE TABLE tasklist(
      id INTEGER PRIMARY KEY NOT NULL,
      name TEXT NOT NULL,
      user_id INTEGER,
      FOREIGN KEY(user_id) REFERENCES user(id)
    );

    INSERT INTO tasklist (id, name, user_id) VALUES (1, 'Complete the test task for Ruby Garage', 1);
    INSERT INTO tasklist (id, name, user_id) VALUES (2, 'My secondary tasklist', 1);
    INSERT INTO tasklist (id, name, user_id) VALUES (3, 'Complete the test task for Ruby Garage', 2);

    DROP TABLE IF EXISTS task;
    CREATE TABLE task(
      id INTEGER PRIMARY KEY NOT NULL,
      name TEXT NOT NULL,
      tasklist_id INTEGER,
      FOREIGN KEY(tasklist_id) REFERENCES tasklist(id)
    );

    INSERT INTO task (id, name, tasklist_id) VALUES (1, 'To complete python backend', 1);
    INSERT INTO task (id, name, tasklist_id) VALUES (2, 'Implement HTML markup', 1);
    INSERT INTO task (id, name, tasklist_id) VALUES (3, 'Integrate with SQLite database', 1);
    INSERT INTO task (id, name, tasklist_id) VALUES (4, 'The task from secondary tasklist', 2);
    INSERT INTO task (id, name, tasklist_id) VALUES (5, 'Yeah one more task', 2);
    """)