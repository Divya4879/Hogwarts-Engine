import random

class Wizard:
    def __init__(self, name: str, house):
        self.name = name
        self.house = house
        self.__house_points = 0

    def get_house_points(self):
        return self.__house_points

    def update_house_points(self, points: int):
        self.__house_points += points

    def duel(self, opponent: 'Wizard'):
        pass


class Student(Wizard):
    total_students = 0 # Class Variable (Global tally)
    def __init__(self, name: str, house: str, year: int):
        super().__init__(name, house) # Parent builds the base wizard
        self.year = year              # Child adds the specific student stuff
        self.__energy = 100
        
        # 2. Increment the global tally every time a student is born
        Student.total_students += 1

    @classmethod
    def sort_new_arrival(cls, name: str, year: int) -> Student:
        """Randomly assigns a house and generates a new Student object."""
        houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']

        chosen_house = random.choice(houses)
        return cls(name, chosen_house, year)

    @property
    def energy(self) -> int:
        """The Getter. Allows you to type: print(harry.energy)"""
        return self.__energy

    def modify_energy(self, amount: int) -> None:
        """Pass negative numbers for damage, positive for healing."""
        if self.__energy + amount < 0:
            self.__energy = 0
        elif self.__energy + amount > 100:
            self.__energy = 100
        else:
            self.__energy += amount

    def duel(self, opponent: 'Wizard')-> None:
        if isinstance(opponent, Student):
            opponent.modify_energy(-20)
            print(f"\n{self.name} defeated {opponent.name} in their duel.\n")
        elif isinstance(opponent, Professor):
            print(f"{self.name} was defeated by Professor {opponent.name} in their duel.")



class Professor(Wizard):
    def __init__(self, name: str, house, subject_taught: str):
        super().__init__(name, house)
        self.subject_taught = subject_taught

    def award_points(self, student, points: int): # use student here, not Student. 
        # You're only using a specific object of the Subject class here, not the whole class itself.
        student.update_house_points(points)


    def duel(self, opponent: 'Wizard') -> None:
        if isinstance(opponent, Student):
            opponent.modify_energy(-100)
            print(f"Professor {self.name} effortlessly disarmed {opponent.name}.")
        elif isinstance(opponent, Professor):
            print(f"Professor {self.name} and Professor {opponent.name} duelled to a magnificent draw!")

