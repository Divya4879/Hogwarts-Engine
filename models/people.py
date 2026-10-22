class Wizard:
    def __init__(self, name: str, house: str):
        self.name = name
        self.house = house
        self.__house_points = 0

    def get_house_points(self):
        return self.__house_points

    def update_house_points(self, points: int):
        self.__house_points += points


class Student(Wizard):
    def __init__(self, name: str, house: str, year: int):
        super().__init__(name, house) # Parent builds the base wizard
        self.year = year              # Child adds the specific student stuff

class Professor(Wizard):
    def __init__(self, name: str, house: str, subject_taught: str):
        super().__init__(name, house)
        self.subject_taught = subject_taught

    def award_points(self, student: str, points: int): # use student here, not Student. 
        # You're only using a specific object of the Subject class here, not the whole class itself.
        student.update_house_points(points)
