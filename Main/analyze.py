#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def daily():
    # returns all habits with category daily
    try:
        import sqlite3
        sqlVerbindung=sqlite3.connect("Main/habits_data.db")
        zeiger=sqlVerbindung.cursor()
        command="""SELECT * FROM habits_data WHERE ("Category")='daily'"""
        zeiger.execute(command)
        Aufzeichnung=zeiger.fetchall()
        # print each row
        for row in Aufzeichnung:
            print(row)
        sqlVerbindung.commit()
        zeiger.close()
    except sqlite3.Error as error:
        print("Failed to access data from sqlite table.", error)
    finally:
        sqlVerbindung.close()
        
def weekly():
     # returns all habits with category weekly
    try:
        import sqlite3
        sqlVerbindung=sqlite3.connect("Main/habits_data.db")
        zeiger=sqlVerbindung.cursor()
        command="""SELECT * FROM habits_data WHERE ("Category")='weekly'"""
        zeiger.execute(command)
        Aufzeichnung=zeiger.fetchall()
        # print each row
        for row in Aufzeichnung:
            print(row)
        sqlVerbindung.commit()
        zeiger.close()
    except sqlite3.Error as error:
        print("Failed to access data from sqlite table.", error)
    finally:
        sqlVerbindung.close()

def monthly():
     # returns all habits with category monthly
    try:
        import sqlite3
        sqlVerbindung=sqlite3.connect("Main/habits_data.db")
        zeiger=sqlVerbindung.cursor()
        command="""SELECT * FROM habits_data WHERE ("Category")='monthly'"""
        zeiger.execute(command)
        Aufzeichnung=zeiger.fetchall()
        # print each row
        for row in Aufzeichnung:
            print(row)
        sqlVerbindung.commit()
        zeiger.close()
    except sqlite3.Error as error:
        print("Failed to access data from sqlite table.", error)
    finally:
        sqlVerbindung.close()

def longest():
     # returns habit(s) with longest streak
    try:
        import sqlite3
        sqlVerbindung=sqlite3.connect("Main/habits_data.db")
        zeiger=sqlVerbindung.cursor()
        command="""SELECT Name, MAX(longest_streak) FROM habits_data"""
        zeiger.execute(command)
        Aufzeichnung=zeiger.fetchall()
        # print each row
        for row in Aufzeichnung:
            print(row)
        sqlVerbindung.commit()
        zeiger.close()
    except sqlite3.Error as error:
        print("Failed to access data from sqlite table.", error)
    finally:
        sqlVerbindung.close()

