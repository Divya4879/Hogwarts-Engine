from database import generate_hogwarts_data

db = generate_hogwarts_data()

houses = db['Houses']
subjects = db['Subjects']
students = db['Students']
professors = db['Professors']

snape = professors[0]
harry = students[0]
snape.award_points(harry, -20)
print(harry.get_house_points())


for house in houses:
    print(f'{house.name}: {house.get_house_score()} points.')