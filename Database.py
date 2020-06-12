import sqlite3
import os
from User import User

class Database:
    def __init__(self, flask_app):
        self.conn = sqlite3.connect(flask_app.root_path+'/database.sqlite')
    
    def create_table(self):
        cur = self.conn.cursor()
        users_table = """
        CREATE TABLE IF NOT EXISTS users (
            mail TEXT PRIMARY KEY
        )
        """
        cur.execute(users_table)
    
    def insert_user(self, user):
        cur = self.conn.cursor()
        user_sql = "INSERT INTO users (mail) VALUES (?)"
        cur.execute(user_sql, (user.mail))
        self.conn.commit()
