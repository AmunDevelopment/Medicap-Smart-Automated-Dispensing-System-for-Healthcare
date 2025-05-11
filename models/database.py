import os
import sqlite3

class Database:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.DB_PATH = os.path.join('src', 'data','ADC.db')
            cls._instance.connect = sqlite3.connect(cls._instance.DB_PATH)
            cls._instance.cursor = cls._instance.connect.cursor()
        return cls._instance

    def close(self):
        self.connect.close()