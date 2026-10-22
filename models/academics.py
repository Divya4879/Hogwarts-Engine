class Subject:
    def __init__(self, name: str, professor_name: str):
        self.name = name
        self.professor_name = professor_name
        self.students_grade = {}

    def add_grade(self, student_name: str, score: int):
        if student_name in self.students_grade:
            self.students_grade[student_name].append(score)
        else:
            self.students_grade[student_name] = [score]

    def get_average(self, student_name: str):
        if student_name in self.students_grade:
            return sum(self.students_grade)/len(self.students_grade[student_name])
        return 0

    def __str__(self):
        return f'{self.name} is taught by Professor {self.professor_name}.'

    def __len__(self):
        return len(self.students_grade)


class House:
    def __init__(self, name: str, head_of_house: str):
        self.name = name
        self.head_of_house = head_of_house
        self.roster = []

    def add_student(self, student):
        self.roster.append(student)

    def get_house_score(self):
        score = 0
        for student in self.roster:
            score += student.get_house_points()
        return score
