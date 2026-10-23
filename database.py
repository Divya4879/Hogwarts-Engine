from models.academics import Subject, House
from models.creatures import Creature
from models.people import Student, Professor

def generate_hogwarts_data() -> dict:
    gryffindor = House('Gryffindor', 'Minerva McGonagall')
    slytherin = House('Slytherin', 'Severus Snape')
    ravenclaw = House('Ravenclaw', 'Filius Flitwick')
    hufflepuff = House('Hufflepuff', 'Pomona Sprout')

    mcgonagall = Professor('Minerva McGonagall', 'Gryffindor', 'Transfiguration')
    snape = Professor('Severus Snape', 'Slytherin', 'Potions')
    flitwick = Professor('Filius Flitwick', 'Ravenclaw', 'Charms')
    sprout = Professor('Pomona Sprout', 'Hufflepuff', 'Herbology')
    lupin = Professor('Remus Lupin', 'Gryffindor', 'Defense Against the Dark Arts')
    babbling = Professor('Bathsheda Babbling', 'Ravenclaw', 'Ancient Runes')
    vector = Professor('Septima Vector', 'Ravenclaw', 'Arithmancy')
    hagrid = Professor('Rubeus Hagrid', 'Gryffindor', 'Care of Magical Creatures')

    harry = Student('Harry Potter', 'Gryffindor', 3)
    draco = Student('Draco Malfoy', 'Slytherin', 3)
    luna = Student('Luna Lovegood', 'Ravenclaw', 2)
    cedric = Student('Cedric Diggory', 'Hufflepuff', 5)

    unicorn = Creature('Unicorn', 1)
    niffler = Creature('Niffler', 1)
    bowtruckle = Creature('Bowtruckle', 2)
    hippogriff = Creature('Hippogriff', 3)
    acromantula = Creature('Acromantula', 4)
    dragon = Creature('Hungarian Horntail', 5)
    basilisk = Creature('Basilisk', 5)


    gryffindor.add_student(harry)
    slytherin.add_student(draco)
    ravenclaw.add_student(luna)
    hufflepuff.add_student(cedric)

    potions = Subject('Potions', 'Severus Snape')
    transfiguration = Subject('Transfiguration', 'Minerva McGonagall')
    charms = Subject('Charms', 'Filius Flitwick')
    dada = Subject('Defense Against the Dark Arts', 'Remus Lupin')
    herbology = Subject('Herbology', 'Pomona Sprout')
    ancient_runes = Subject('Ancient Runes', 'Bathsheda Babbling')
    arithmancy = Subject('Arithmancy', 'Septima Vector')
    care_of_magical_creatures = Subject('Care of Magical Creatures', 'Hagrid')


    potions.add_grade(harry, 85)          
    transfiguration.add_grade(harry, 75)  
    dada.add_grade(harry, 100)            
    charms.add_grade(harry, 75)           
    herbology.add_grade(harry, 90)        
    care_of_magical_creatures.add_grade(harry, 95)


    potions.add_grade(draco, 96)          
    transfiguration.add_grade(draco, 84)  
    charms.add_grade(draco, 82)           
    dada.add_grade(draco, 78)             
    herbology.add_grade(draco, 76)        
    care_of_magical_creatures.add_grade(draco, 60)
    ancient_runes.add_grade(draco, 89)    


    potions.add_grade(luna, 72)           
    transfiguration.add_grade(luna, 78)   
    charms.add_grade(luna, 92)            
    dada.add_grade(luna, 80)              
    herbology.add_grade(luna, 88)         


    potions.add_grade(cedric, 88)        
    transfiguration.add_grade(cedric, 95)  
    charms.add_grade(cedric, 94)          
    dada.add_grade(cedric, 92)            
    herbology.add_grade(cedric, 90)       
    care_of_magical_creatures.add_grade(cedric, 93)
    arithmancy.add_grade(cedric, 85) 

    return {
        'Houses': [gryffindor, slytherin, ravenclaw, hufflepuff],
        'Subjects': [
            potions, transfiguration, charms, dada, herbology,
            ancient_runes, arithmancy, care_of_magical_creatures
            ],
        'Students' : [harry, draco, luna, cedric],
        'Professors': [
            snape, mcgonagall, flitwick, sprout, lupin, babbling, vector, hagrid
            ],
        'Creatures': [
            unicorn, niffler, bowtruckle, hippogriff, acromantula, dragon, basilisk
            ]
    }