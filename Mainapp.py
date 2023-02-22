#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Habit Tracker"""
class Habits():
    """Habit class"""
    
    def __init__(self):
        print('\nWelcome to Habit Tracker')
    
    def newtable(self):
        """create new table"""
        from Main import predefinedhabits
        predefinedhabits.pretable()
    
    def predef(self):
        """create 5 predefinde habits"""
        from Main import predefinedhabits
        predefinedhabits.prehabits()
        
    def createnew(self):
        "user creates new habit"
        from Main import createnew
        createnew.habitnew()
        
    def showtable(self):
        "table is shown"
        try:
            import sqlite3
            sqlVerbindung=sqlite3.connect("Main/habits_data.db")
            zeiger=sqlVerbindung.cursor()
            command="""SELECT * FROM habits_data"""
            zeiger.execute(command)
            Aufzeichnung=zeiger.fetchall()
            kopf=['ID', 'Name', 'Category', 'current_streak', 'last_streak', 'longest_streak','set_goal', 'goal_reached']
            print("\n")
            print(kopf)
                # print each row
            for row in Aufzeichnung:
                print(row)
            sqlVerbindung.commit()
            zeiger.close()
        except sqlite3.Error as error:
            print("Failed to access data from sqlite table.", error)
        finally:
            sqlVerbindung.close()
        
    def userselect(self):
        "user selects habit via ID"
        from Main import user
        user.selecthabit()
                
    def usercheck(self):
        "user checks streak"
        from Main import user
        user.check()
        
    def useredit(self):
        "user edits habit"
        from Main import user
        user.edit()
        
    def userdelete(self):
        "user deletes habit"
        from Main import user
        user.delete()
        
    def analdaily(self):
        "shows daily habits"
        from Main import analyze
        analyze.daily()
        
    def analweekly(self):
        "shows weekly habits"
        from Main import analyze
        analyze.weekly()
        
    def analmonthly(self):
        "shows monthly habits"
        from Main import analyze
        analyze.monthly()
        
    def anallongest(self):
        "shows longest streak"
        from Main import analyze
        analyze.longest()        
        
        
    

# Main Menu
def main_menu():
    """Main Menu"""
    myhabits=Habits()
    myhabits.newtable()
    # use test data
    schleife1=True
    while schleife1==True:
        prechoice=input("\n Predefine Habits for testing? Y/N ")
        if prechoice.upper()=='Y':
            myhabits.predef()
            schleife1=False
        elif prechoice.upper()=='N':
            break
        else:
            print("\n Wrong input. Try again.")
            schleife1=True
        
    # load and show table
    myhabits.showtable()
    
    choice = ''
    #loop until quit
    while choice.lower() != 'q':
        print("\nEnter 1 to check, edit or delete a habit.")
        print("Enter 2 to create a new habit.")
        print("Enter 3 to analyze your habits.")
        print("Enter 4 to show habits.")
        print("Enter q to quit the program.")
        
        choice=input("\n Your Choice: ")
        
        # users choice
        if choice=='1':
            
            # submenu
            choice_1 = ''
            while choice_1.lower() != 'x':
                print("\nEnter 1 to check a habit.")
                print("Enter 2 to edit a habit.")
                print("Enter 3 to delete a habits.")
                print("Enter x to exit to the main menu.")
                
                # users choice_1
                choice_1=input("\n Your choice: ")
            
                if choice_1=='1':
                    myhabits.usercheck()
                elif choice_1=='2':
                    myhabits.useredit()
                elif choice_1=='3':
                    myhabits.userdelete()
                elif choice_1=='x':
                    print("\n")
                else:
                    print("\n Wrong input, please input correct.\n")
        
  
        elif choice=='2':         # create new habit
            myhabits.createnew()
        elif choice=='3':         # analyzing habits
            
            choice_2 = ''
            while choice_2.lower() != 'x':
                print("\nEnter 1 to show daily habits.")
                print("Enter 2 to show weekly habits.")
                print("Enter 3 to show monthly habits.")
                print("Enter 4 to show longest streak of all habits.")
                print("Enter x to exit to the main menu.")
                
                # users choice_2
                choice_2=input("\n Your choice: ")
            
                if choice_2=='1':
                    myhabits.analdaily()
                elif choice_2=='2':
                    myhabits.analweekly()
                elif choice_2=='3':
                    myhabits.analmonthly()
                elif choice_2=='4':
                    myhabits.anallongest()
                elif choice_2=='x':
                    print("\n")
                else:
                    print("\n Wrong input, please input correct.\n")
        elif choice=='4':
            myhabits.showtable()
        elif choice=='q':
            print("\n Bye bye!")
        else:
            print("\n Wrong input, please input correct.\n")
        
main_menu()

