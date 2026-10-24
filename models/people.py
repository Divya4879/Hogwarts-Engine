import random

class Wizard:
    """
    A base class representing a magic user in the Hogwarts universe.

    Attributes:
        name (str): The wizard's full name.
        house (str): The Hogwarts house the wizard belongs to.
    """
    def __init__(self, name: str, house: str):
        self.name = name
        self.house = house
        self.__house_points = 0

    def get_house_points(self)-> int:
        """
        Retrieves the wizard's current house points.

        Returns:
            int: The total house points earned.
        """
        return self.__house_points

    def update_house_points(self, points: int)-> None:
        """
        Modifies the wizard's house points.

        Args:
            points (int): The number of points to add (can be negative for point deductions).
        """
        self.__house_points += points

    def duel(self, opponent: 'Wizard'):
        pass


class Student(Wizard):
    """
    Represents a student enrolled at Hogwarts.

    Attributes:
        total_students (int): A class-level tracker of the total student population.
        year (int): The student's current academic year.
    """
    total_students = 0 # Class Variable (Global tally)
    def __init__(self, name: str, house: str, year: int):
        super().__init__(name, house) # Parent builds the base wizard
        self.year = year              # Child adds the specific student stuff
        self.__energy = 100
        
        # 2. Increment the global tally every time a student is born
        Student.total_students += 1

    @classmethod
    def sort_new_arrival(cls, name: str, year: int) -> 'Student':
        """
        Alternative constructor that randomly sorts a new arrival into a House.

        Args:
            name (str): The name of the new student.
            year (int): The academic year of the new student.

        Returns:
            Student: A newly instantiated Student object with a randomly assigned House.
        """
        houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']

        chosen_house = random.choice(houses)
        return cls(name, chosen_house, year)

    @property
    def energy(self) -> int:
        """
        Retrieves the student's current energy level.

        Returns:
            int: The student's energy, bounded between 0 and 100.
        """
        # The Getter. Allows you to type: print(harry.energy)
        return self.__energy

    def modify_energy(self, amount: int) -> None:
        """
        Adjusts the student's energy level safely, enforcing the 0-100 bounds.

        Args:
            amount (int): The amount to change the energy by (negative for damage).
        """
        if self.__energy + amount < 0:
            self.__energy = 0
        elif self.__energy + amount > 100:
            self.__energy = 100
        else:
            self.__energy += amount

    def duel(self, opponent: 'Wizard')-> None:
        """
        Executes a student-level duel. Students can damage other students,
        but will automatically lose if they duel a Professor.

        Args:
            opponent (Wizard): The wizard being challenged.
        """
        if isinstance(opponent, Student):
            opponent.modify_energy(-20)
            print(f"\n{self.name} defeated {opponent.name} in their duel.\n")
        elif isinstance(opponent, Professor):
            print(f"{self.name} was defeated by Professor {opponent.name} in their duel.")



class Professor(Wizard):
    """
    Represents a professor teaching at Hogwarts.

    Attributes:
        subject_taught (str): The academic subject taught by the professor.
    """
    def __init__(self, name: str, house, subject_taught: str):
        super().__init__(name, house)
        self.subject_taught = subject_taught

    def award_points(self, student, points: int)-> None: # use student here, not Student. 
        """
        Grants or deducts house points from a specific student.

        Args:
            student (Student): The student receiving the point adjustment.
            points (int): The number of points to award or deduct.
        """
        # You're only using a specific object of the Subject class here, not the whole class itself.
        student.update_house_points(points)


    def duel(self, opponent: 'Wizard') -> None:
        """
        Executes a professor-level duel. Professors instantly defeat students,
        but duel other professors to a draw.

        Args:
            opponent (Wizard): The wizard being challenged.
        """
        if isinstance(opponent, Student):
            opponent.modify_energy(-100)
            print(f"Professor {self.name} effortlessly disarmed {opponent.name}.")
        elif isinstance(opponent, Professor):
            print(f"Professor {self.name} and Professor {opponent.name} duelled to a magnificent draw!")