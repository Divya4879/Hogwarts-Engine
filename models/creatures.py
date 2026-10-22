from abc import ABC, abstractmethod

class MagicalEntity(ABC):
    # This decorator forces any child class to implement this exact method.
    @abstractmethod
    def interact(self, student: str) -> None:
        pass # We leave this blank. The child class must write the actual code.


# 2. The Actual Object (The Child Class)
class Creature(MagicalEntity):
    def __init__(self, name: str, danger_level: int):
        self.name = name
        self.danger_level = danger_level

    # If we delete this method, Python will crash. 
    def interact(self, student) -> None:
        if self.danger_level > 3:
            student.update_house_points(-20)
            print(f'{self.name} attacked {student.name}')
        else:
            print(f'{student.name} safely observed {self.name}, a creature.')