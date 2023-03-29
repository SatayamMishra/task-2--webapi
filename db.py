import sqlite3


conn = sqlite3.connect("TA.db")

print("database open successfully")


conn.execute("CREATE TABLE TA (id TEXT, native_english_speaker BOOLEAN NOT NULL, course_instructor TEXT NOT NULL, course TEXT NOT NULL, semester TEXT NOT NULL, class_size INTEGER NOT NULL, performance_score INTEGER NOT NULL)")

print("table created successfully")
 

conn.close()