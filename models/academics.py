class Subject:
    """
    Represents an academic subject taught at Hogwarts.

    Attributes:
        name (str): The name of the subject (e.g., Potions).
        professor_name (str): The professor teaching the course.
        students_grade (dict): A mapping of student names to their list of scores.
    """
    def __init__(self, name: str, professor_name: str):
        self.name = name
        self.professor_name = professor_name
        self.students_grade = {}

    def add_grade(self, student_name: str, score: int)-> None:
        """
        Assigns a numerical grade to a specific student.

        Args:
            student_name (str): The name of the student.
            score (int): The grade received.
        """
        if student_name in self.students_grade:
            self.students_grade[student_name].append(score)
        else:
            self.students_grade[student_name] = [score]


    def __str__(self):
        """Returns a readable string representation of the subject."""
        return f'{self.name} is taught by Professor {self.professor_name}.'

    def __len__(self):
        """Returns the total number of students enrolled in the subject."""
        return len(self.students_grade)


class House:
    """
    Represents a Hogwarts House.

    Attributes:
        name (str): The name of the House (e.g., Gryffindor).
        head_of_house (str): The professor managing the House.
        roster (list): A collection of Student objects belonging to the House.
    """
    def __init__(self, name: str, head_of_house: str):
        self.name = name
        self.head_of_house = head_of_house
        self.roster = []

    def add_student(self, student)-> list:
        """
        Enrolls a student into the House roster.

        Args:
            student (Student): The instantiated Student object being added.
        """
        self.roster.append(student)

    def get_house_score(self)-> int:
        """
        Calculates the total house points earned by all enrolled students.

        Returns:
            int: The cumulative house points of the House.
        """
        score = 0
        for student in self.roster:
            score += student.get_house_points()
        return score