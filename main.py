from database import generate_hogwarts_data
import sys
import random

db = generate_hogwarts_data()

houses = db['Houses']
subjects = db['Subjects']
students = db['Students']
professors = db['Professors']
creatures = db['Creatures']

harry = students[0]
draco = students[1]
luna = students[2]
cedric = students[3]

snape = professors[0]
macgonagall = professors[1]
flitwick = professors[2]
sprout = professors[3]
lupin = professors[4]
hagrid = professors[-1]

unicorn = creatures[0]
niffler = creatures[1]
bowtruckle = creatures[2]
hippogriff = creatures[3]
acromantula = creatures[4]
dragon = creatures[5]
basilisk = creatures[6]


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
            print("\n******* HOGWARTS HOUSE STANDINGS *******\n")
            for house in houses:
                print(f"\t{house.name}: {house.get_house_score()}")

        elif choice == 2:
            for house in houses:
                print(f"{house.name.upper()} HOUSE:")
                print(f"Head of House: {house.head_of_house}")
                print("Students:")
                for student in house.roster:
                    print(student.name)
                print()

        elif choice == 3:
            print('Students:\n')
            for student in students:
                print(student.name)

            print('Professors\n')
            for professor in professors:
                print(professor.name)

            print("This is the list of students & professors in Hogwarts as of now.\n")

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


            fighter_1.duel(fighter_2)

        elif choice == 4:
            print("\nWELCOME TO THE FORBIDDEN FOREST!!\n You're WARNED!!\n")

            student_choice = input('Which naghty student are you?: ').lower()
            naughty_student = None

            for student in students:
                if student_choice in student.name.lower():
                    naughty_student = student
                    break

            if not naughty_student:
                print("This student isn't a student here.")
                continue


            for i in range(3):
                creature_facing = random.choice(creatures)
                creature_facing.interact(naughty_student)
      

        elif choice == 5:
            sys.exit(0)