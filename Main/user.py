#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def check():
    import sqlite3
    sqlVerbindung=sqlite3.connect("Main/habits_data.db")
    zeiger=sqlVerbindung.cursor()
    Aufzeichnung=zeiger.fetchall()
    laenge=len(Aufzeichnung)
    print("\n Choose a habit by typing their ID. ")
    # ID inquiry
    while True:
        userID=input("\n Your choice: ")
        try:
            userID=int(userID)
        except ValueError:
            print("\n No valid ID. Try again.")
        except userID>laenge:
            print("\n Your input ID does not exist. Try again.")
        else:
            break
    userID=int(userID)
    schleife1=True
    while schleife1==True:        
        check_1=input("\n Add to your streak? Y/N ")
        if check_1.upper()=='N':
            schleife2=True
            while schleife2==True:
                check_2=input("\n Reset streak? Y/N ")
                if check_2.upper()=='Y':
                    # reset streak and set current streak as last streak
                    command1=(f'''SELECT current_streak FROM habits_data WHERE ID={userID} AND ID IS NOT NULL;''')
                    zeiger.execute(command1)
                    Aufzeichnung=zeiger.fetchone()
                        # tuple to int
                    newlast=int(Aufzeichnung[0])
                    # check goal
                    command4=(f'''SELECT set_goal FROM habits_data WHERE ID={userID} AND ID IS NOT NULL;''')
                    zeiger.execute(command4)
                    Aufzeichnung=zeiger.fetchone()
                        # tuple to int
                    goaly=int(Aufzeichnung[0])
                    if newlast>=goaly:
                        command5=(f'''UPDATE habits_data SET goal_reached=goal_reached+1 WHERE ID={userID} AND ID IS NOT NULL;''')
                        zeiger.execute(command5)
                    # check longest streak
                    command6=(f'''SELECT longest_streak FROM habits_data WHERE ID={userID} AND ID IS NOT NULL;''')
                    zeiger.execute(command6)
                    Aufzeichnung=zeiger.fetchone()
                        # tuple to int
                    longer=int(Aufzeichnung[0])
                    if newlast>longer:
                        command7=(f'''UPDATE habits_data SET longest_streak={newlast} WHERE ID={userID} AND ID IS NOT NULL;''')
                        zeiger.execute(command7)
                    # update last streak
                    command2=(f'''UPDATE habits_data SET last_streak={newlast} WHERE ID={userID} AND ID IS NOT NULL;''')
                    zeiger.execute(command2)
                    #update current streak
                    command3=(f'''UPDATE habits_data SET current_streak=0 WHERE ID={userID} AND ID IS NOT NULL;''')
                    zeiger.execute(command3)
                    sqlVerbindung.commit()
                    schleife2=False
                elif check_2.upper()=='N':
                    break
                else:
                    print("\n Wrong input. Try again.")
                    schleife2=True
            schleife1=False
        elif check_1.upper()=='Y':
            # add to streak
            command=(f'''UPDATE habits_data SET current_streak=current_streak+1 WHERE ID={userID} AND ID IS NOT NULL;''')
            zeiger.execute(command)
            sqlVerbindung.commit()
            schleife1=False
        else:
            print("\n Wrong input. Try again.")
            schleife1=True
    zeiger.close()
    sqlVerbindung.close()     
        
            

def edit():
    import sqlite3
    sqlVerbindung=sqlite3.connect("Main/habits_data.db")
    zeiger=sqlVerbindung.cursor()
    Aufzeichnung=zeiger.fetchall()
    laenge=len(Aufzeichnung)
    print("\n Choose a habit by typing their ID. ")
    while True:
        userID=input("\n Your choice: ")
        try:
            userID=int(userID)
        except ValueError:
            print("\n No valid ID. Try again.")
        except userID>laenge:
            print("\n Your input ID does not exist. Try again.")
        else:
            break
    schleife1=True
    while schleife1==True:
        edit_1=input("\n Edit Name? Y/N ")
        if edit_1.upper()=='N':
            schleife2=True
            while schleife2==True:
                edit_2=input("\n Edit Goal? Y/N ")
                if edit_2.upper()=='Y':
                    # edit goal
                    while True:
                        setgoal=input("\n Set new goal: ")
                        try:
                            setgoal=int(setgoal)
                        except ValueError:
                            print("No valid input. Try again.")
                        else:
                            break
                    command=(f'''UPDATE habits_data SET set_goal={setgoal} WHERE ID={userID} AND ID IS NOT NULL;''')
                    zeiger.execute(command)
                    command2=(f'''UPDATE habits_data SET goal_reached=0 WHERE ID={userID} AND ID IS NOT NULL;''')
                    zeiger.execute(command2)
                    sqlVerbindung.commit()
                    schleife2=False
                elif edit_2.upper()=='N':
                    break
                else:
                    print("\n Wrong input. Try again.")
                    schleife2=True
            schleife1=False
        elif edit_1.upper()=='Y':
            # edit name
            newname=input("\n Choose new name: ")
            command=(f'''UPDATE habits_data SET Name='{newname}' WHERE ID={userID} AND ID IS NOT NULL;''')
            zeiger.execute(command)
            sqlVerbindung.commit()
            schleife1=False
        else:
            print("\n Wrong input. Try again.")
            schleife1=True
    zeiger.close()
    sqlVerbindung.close()

    
def delete():
    import sqlite3
    sqlVerbindung=sqlite3.connect("Main/habits_data.db")
    zeiger=sqlVerbindung.cursor()
    Aufzeichnung=zeiger.fetchall()
    laenge=len(Aufzeichnung)
    print("\n Choose a habit by typing their ID. ")
    while True:
        userID=input("\n Your choice: ")
        try:
            userID=int(userID)
        except ValueError:
            print("\n No valid ID. Try again.")
        except userID>laenge:
            print("\n Your input ID does not exist. Try again.")
        else:
            break
    command=(f'''DELETE FROM habits_data WHERE ID={userID} AND ID IS NOT NULL;''')
    zeiger.execute(command)
    command2=(f'''UPDATE habits_data SET ('ID')=(ID)-1 WHERE ID>{userID};''')
    zeiger.execute(command2)
    sqlVerbindung.commit()
    print("\n Habit deleted.")
    zeiger.close()
    sqlVerbindung.close()

