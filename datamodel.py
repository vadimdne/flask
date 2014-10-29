__author__ = 'vti'
import sqlite3

DATABASE = "tasks.db"

conn = sqlite3.connect(DATABASE, check_same_thread=False)
conn.isolation_level = None
cur = conn.cursor()

if __name__ == "__main__":
    cur.executescript("""
    DROP TABLE IF EXISTS user;
    CREATE TABLE user(
      id INT PRIMARY KEY NOT NULL,
      username TEXT NOT NULL,
      salt TEXT NOT NULL,
      hash TEXT NOT NULL
    );

    DROP TABLE IF EXISTS tasklist;
    CREATE TABLE tasklist(
      id INTEGER PRIMARY KEY NOT NULL,
      name TEXT NOT NULL,
      user_id INTEGER,
      FOREIGN KEY(user_id) REFERENCES user(id)
    );

    DROP TABLE IF EXISTS task;
    CREATE TABLE task(
      id INTEGER PRIMARY KEY NOT NULL,
      name TEXT NOT NULL,
      tasklist_id INTEGER,
      FOREIGN KEY(tasklist_id) REFERENCES tasklist(id)
    );

    DROP TABLE IF EXISTS session;
    CREATE TABLE session(
      id INTEGER NOT NULL,
      start_time TIMESTAMP NOT NULL,
      end_time TIMESTAMP NOT NULL,
      user_id INTEGER,
      FOREIGN KEY(user_id) REFERENCES user(id)
    );

    INSERT INTO user (id, username, salt, hash) VALUES (1, 'vadim', '12d11ce1a7034ace98524615686882e2', 'bd95de4d6c2127db6132684798c1a8fdc9fa861a612b01f3f932caf58576a02991d2b16e919058d1bbd45586ba8cb985c121101d4574f4270d04d37e582a8464');
    INSERT INTO user (id, username, salt, hash) VALUES (2, 'roman', '981e31eede3b4735b14621137e270249', 'b2f58a58cd6cd8eb7cc99180904cd579756ee8b7f77557da38890fe00ed43d42da33d21dbdee35e8651683ee8ce073abb81f1e8015f07162a1bc61e4f96c2aaa');
    INSERT INTO user (id, username, salt, hash) VALUES (3, 'igor', '8737062506eb4be78e3466ccc95a0c18', '3258b9e2ad1f2b4bec0334951f96dd52d831ed287e40a629bf3a39a8ba0fe529bb9ae3b103702b7f372e6d0442b523ecfffd29f252ef95d4f9e793087bae6e1d');

    INSERT INTO tasklist (id, name, user_id) VALUES (1, 'Complete the test task for Ruby Garage', 1);
    INSERT INTO tasklist (id, name, user_id) VALUES (2, 'My secondary tasklist', 1);
    INSERT INTO tasklist (id, name, user_id) VALUES (3, 'Complete the test task for Ruby Garage', 2);

    INSERT INTO task (id, name, tasklist_id) VALUES (1, 'To complete python backend', 1);
    INSERT INTO task (id, name, tasklist_id) VALUES (2, 'Implement HTML markup', 1);
    INSERT INTO task (id, name, tasklist_id) VALUES (3, 'Integrate with SQLite database', 1);
    INSERT INTO task (id, name, tasklist_id) VALUES (4, 'The task from secondary tasklist', 2);
    INSERT INTO task (id, name, tasklist_id) VALUES (5, 'Yeah one more task', 2);
    """)