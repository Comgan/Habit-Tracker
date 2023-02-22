#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#creates table habits_data via sqlite3

def pretable():
    try:
        import sqlite3
        sqlVerbindung=sqlite3.connect("Main/habits_data.db")
        zeiger=sqlVerbindung.cursor()
        command="""CREATE TABLE IF NOT EXISTS 'habits_data' (
        'ID' INTEGER,
        'Name' varchar(20),
        'Category' varchar(10),
        'current_streak' INTEGER,
        'last_streak' INTEGER,
        'longest_streak' INTEGER,
        'set_goal' INTEGER,
        'goal_reached' INTEGER,
        PRIMARY KEY("ID" AUTOINCREMENT)
        )"""
        zeiger.execute(command)
        
        #if already exists
        Aufzeichnung=zeiger.fetchall()
        sqlVerbindung.commit()
        zeiger.close()
    except sqlite3.Error as error:
        print("Failed to access data from sqlite table.", error)
    finally:
        sqlVerbindung.close()
            
            
# creating 5 predefined habits in habits_data
def prehabits():
    import sqlite3
    sqlVerbindung=sqlite3.connect("Main/habits_data.db")
    zeiger=sqlVerbindung.cursor()
    predefhabits = [('1', 'no sweets', 'daily', 5, 10, 10, 30, 1),
                    ('2', 'no alkohol', 'daily', 14, 7, 25, 90, 0),
                    ('3', 'running', 'weekly', 2, 5, 6, 14, 1),
                    ('4', 'no smoking', 'daily', 18, 12, 65, 30, 3),
                    ('5', 'clean windows', 'monthly', 3, 3, 4, 6, 0)]
    zeiger.executemany(
        "INSERT OR REPLACE INTO habits_data ('ID', 'Name', 'Category', 'current_streak', 'last_streak', 'longest_streak','set_goal', 'goal_reached') VALUES(?,?,?,?,?,?,?,?)",
        predefhabits)
        
    sqlVerbindung.commit()
    zeiger.close()
    sqlVerbindung.close()

