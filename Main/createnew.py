#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def habitnew():
    # show current list
    import sqlite3
    sqlVerbindung=sqlite3.connect("Main/habits_data.db")
    zeiger=sqlVerbindung.cursor()
    
    command = """SELECT * FROM habits_data"""
    zeiger.execute(command)
    Aufzeichnung=zeiger.fetchall()
    laenge=len(Aufzeichnung)
    
    # new input
    newID=laenge+1
    streak=0
    title=input("\n Name: ")
    setcategory=input("\n Category (daily, weekly, monthly): ")
    streak_longest=0
    streak_last=0
    goal=input("\n Set a goal: ")
    goaltracker=0
    habits=[(newID, title, setcategory,
             streak, streak_last, streak_longest, goal, goaltracker)]
    zeiger.executemany("INSERT OR REPLACE INTO habits_data VALUES(?,?,?,?,?,?,?,?)", habits)
    sqlVerbindung.commit()
    zeiger.close()
    sqlVerbindung.close()
    

