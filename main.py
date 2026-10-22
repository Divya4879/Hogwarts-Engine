from models.academics import Subject, House
from models.people import *
from models.creatures import Creature

potions = Subject('Potions', 'Severus Snape')
transfiguration = Subject('Transfigurations', 'Minerva McGonagall')

potions.add_grade('Harry James Potter', 85)
potions.add_grade('Hermione Jean Granger', 99)

print(potions)
print(transfiguration)

print(len(potions))
print(len(transfiguration))

harry = Student('Harry James Potter', 'Gryffindor', 3)
snape = Professor('Severus Snape', 'Slytherin', 'Potions')

snape.award_points(harry, -50)
print(harry.get_house_points())

harry.__house_points = 1000
print(harry.get_house_points()) # still the same house points as before.

gryffindor = House("Gryffindor", "Minerva McGonagall")
hermione = Student('Hermione Jean Granger', 'Gryffindor', 3)

gryffindor.add_student(harry)
gryffindor.add_student(hermione)

snape.award_points(harry, -50)

minerva = Professor('Minerva McGonagall', 'Gryffindor', 'Transfigurations')
albus = Professor('Albus Dumbledore', 'Gryffindor', 'Alchemy')

minerva.award_points(hermione, 50)
albus.award_points(harry, 100)

print(gryffindor.get_house_score())

dragon = Creature("Norwegian Ridgeback", 5)
flobberworm = Creature("Flobberworm", 1)

# Test the abstraction contract
dragon.interact(harry)
flobberworm.interact(harry)

# Verify the points deduction
print(f"Harry's points after Care of Magical Creatures: {harry.get_house_points()}")
