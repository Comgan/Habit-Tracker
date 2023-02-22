# Habit-Tracker

- simple habit tracker programed with python373
- database with sqlite3


## **Faetures**

The user can create, edit and delete a habit and analyze existing ones via an options menu.


## **How to use**

When starting the program the user is asked whether he wants to use predefined habits or not. This is for testing reasons.
Afterwards the existing habit table is loaded and displayed and the main menu will appear.

Main menu:
- Enter 1 to check, edit or delete a habit.
- Enter 2 to create a new habit.
- Enter 3 to analyze your habits.
- Enter 4 to show habits.
- Enter q to quit the program.

Depending on the input the program will execute the desired option.

1. Uppon entering '1' a submenu is opened. Here the user can choose between checking, editing or deleting a habit. By inserting the respective habit ID the habit to operate on is chosen.
For checking the user will first be asked whether the streak should be continued by adding to it. If the user decides for 'no' the next question is whether the user wants to reset the streak and updating the habit properties. Properties like reached goal and longest streak will only be updated if the streak is reset.
Editing a streak will ask the user first about editing the name of the chosen habit. If the name shall not be edited the question for editing the set goal will come next. Editing the goal will reset the goal counter.
2. Entering '2' the user will have to input name, category (as in daily, weekly or monthly) and a personal streak goal. The new habit will be added to the end of the habits list.
3. The analyzing tools are diplayed in a submenu where the user can choose between various options.
- Enter 1 to to show daily habits.
- Enter 2 to show weekly habits.
- Enter 3 to show monthly habits.
- Enter 4 to show longest streak of all habits.
- Enter x to exit to the main menu.
4. Choosing '4' in the main menu will result in showing all the existing habits.
