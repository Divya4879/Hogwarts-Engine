"""
Master Controller for the Hogwarts Simulator.
Provides an interactive Command Line Interface (CLI) for users to interact with
the underlying Object-Oriented Hogwarts engine.
"""

from database import generate_hogwarts_data
import sys
import random

# Initialize the database and unpack the master lists

db = generate_hogwarts_data()

houses = db['Houses']
subjects = db['Subjects']
students = db['Students']
professors = db['Professors']
creatures = db['Creatures']


def display_house_standings()-> None:
    """Retrieves and displays the current point standings for all Hogwarts Houses."""
    print("\n******* HOGWARTS HOUSE STANDINGS *******\n")
    for house in houses:
        print(f"\t{house.name}: {house.get_house_score()}")
    print()

def display_house_roster()-> None:
    """Displays the head of house and a list of enrolled students for each House."""
    print()
    for house in houses:
        print(f"{house.name.upper()} HOUSE:")
        print(f"Head of House: {house.head_of_house}")
        print("Students:")
        for student in house.roster:
            print(student.name)
        print()

def duel()-> None:
    """
    Guides the user through selecting two combatants (Students or Professors) 
    from the roster and initiates a magical duel between them.
    """
    print('\nStudents:\n')
    for student in students:
        print(student.name)

    print('\nProfessors\n')
    for professor in professors:
        print(professor.name)

    print("\nThis is the list of students & professors in Hogwarts as of now.\n")
 
    fighter_1_choice = False

    while not fighter_1_choice:
        choice_1 = input('Enter the 1st person in the duel: ').lower()
        fighter_1 = None

        for student in students:
            if choice_1 in student.name.lower():
                fighter_1 = student
                break

        if not fighter_1:
            for professor in professors:
                if choice_1 in professor.name.lower():
                    fighter_1 = professor
                    break
        if fighter_1:
            fighter_1_choice = True
        else:
            print('\nYou need to chose from the list of students & professors you\'re given.\n')
        
    fighter_2_choice = False

    while not fighter_2_choice:
        choice_2 = input('Enter the 2nd person in the duel: ').lower()
        fighter_2 = None

        for student in students:
            if choice_2 in student.name.lower():
                fighter_2 = student
                break

        if not fighter_2:
            for professor in professors:
                if choice_2 in professor.name.lower():
                    fighter_2 = professor
                    break
        if fighter_2:
            fighter_2_choice = True
        else:
            print('\nYou need to chose from the list of students & professors you\'re given.\n')
    
    fighter_1.duel(fighter_2)

def forbidden_forest_entered()-> None:
    """
    Prompts the user to select a student to enter the Forbidden Forest.
    The selected student will interact with three randomly selected creatures.
    """
    print("\nWELCOME TO THE FORBIDDEN FOREST!!\n You're WARNED!!\n")
    
    student_choice = input('Which naughty student are you?: ').lower()
    naughty_student = None

    for student in students:
        if student_choice in student.name.lower():
            naughty_student = student
            break

    if not naughty_student:
        print("You aren't a student here.")
        return
        
    for i in range(3):
        creature_facing = random.choice(creatures)
        print()
        creature_facing.interact(naughty_student)

def continue_exit()-> None:
    """Prompts the user to either continue exploring the simulator or exit the program."""
    exit_loop = input("\nDo you want to explore other choices or quit?\n" \
    "Press y if you want to quit, or any other key to carry on:\n").lower().strip()
    if exit_loop.startswith('y'):
        sys.exit(0)
    else:
        print()
        return 

def main() -> None:
    """The main game loop. Renders the interactive menu and routes user input."""
    while True:
        print("\n====== MINI HOGWARTS SIMULATOR ======\n")
        print("\t1. View House Standings")
        print("\t2. View Class Rosters")
        print("\t3. Initiate a Duel") 
        print("\t4. Enter the Forbidden Forest")
        print("\t5. Exit")
        print("\n=======================================\n")

        correct_choice = False
        while not correct_choice:
            try:
                choice = int(input('Enter any choice from 1-5 to move forward: '))
            except:
                print('Enter a no only, between 1 & 5!\n')
            else:
                correct_choice = True

        else:
            if choice == 1:
                display_house_standings()
                continue_exit()

            elif choice == 2:
                display_house_roster()
                continue_exit()

            elif choice == 3:
                duel()
                continue_exit()

            elif choice == 4:
                forbidden_forest_entered()
                continue_exit()
        

            elif choice == 5:
                sys.exit(0)

# This ensures the game only runs if you execute main.py directly
if __name__ == "__main__":
    main()