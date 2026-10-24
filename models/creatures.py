from abc import ABC, abstractmethod

class MagicalEntity(ABC):
    """
    An abstract base class for all magical entities in the Hogwarts universe.
    Enforces a strict contract that all child classes must define an interact method.
    """
    # This decorator forces any child class to implement this exact method.
    @abstractmethod
    def interact(self, student: 'Student') -> None:
        """
        Defines how the magical entity interacts with a student.
        
        Args:
            student (Student): The instantiated Student object interacting with the entity.
        """
        pass # We leave this blank. The child class must write the actual code.


# 2. The Actual Object (The Child Class)
class Creature(MagicalEntity):
    """
    Represents a magical creature found within the Hogwarts grounds.

    Attributes:
        name (str): The name of the creature (e.g., Hungarian Horntail).
        danger_level (int): The threat level of the creature, determining its behavior.
    """
    def __init__(self, name: str, danger_level: int):
        self.name = name
        self.danger_level = danger_level

    # If we delete this method, Python will crash. 
    def interact(self, student: 'Student') -> None:
        """
        Resolves an encounter between the creature and a student.
        Creatures with a danger level above 3 will attack, reducing energy and house points.

        Args:
            student (Student): The instantiated Student object encountering the creature.
        """
        if self.danger_level > 3:
            student.update_house_points(-20)
            student.modify_energy(-40)
            print(f'{self.name} attacked {student.name}.\n{student.name} lost 20 house points & 40 energy points.')
        else:
            print(f'{student.name} safely observed {self.name}, a creature.')