import random

print("Welcome to storyTime!")



def story_1() :
    character_name = input("Please enter a character name: ")
    character_age = input("Please enter a character age: ")
    character_location = input("Please enter a character location: ")

    print("A CASUAL STORY")
    print("There was once a man named " + character_name + ", ")
    print("he was " + character_age + " years old. ")
    print("he was the resident of " + character_location + ".")
    print("He really liked the name " + character_name + ", ")
    print(" but didn't like being " + character_age + ".")

def story_2() :
    character_name = input("Please enter a character name: ")
    city_name = input("Please enter a city name: ")
    monster_colour = input("Please enter a monster colour: ")
    
    print("A HORROR STORY")
    print("There was a person named" + character_name + ", ")
    print("and he was sitting beside river of  " + city_name + ". ")
    print("Suddenly a " + monster_colour + " colour monster appeared , and "
          + character_name + " ran away.")

def story_3() :
    character_name = input("Please enter a character name: ")
    loss_amount = input("Please enter a loss amount: ")
    robbery_location = input("Please enter a robbery location: ")

    print("A ROBBERY STORY")
    print("There was once a man named " + character_name + ", ")
    print("he was the resident of " + robbery_location + ".")
    print("He lost " + loss_amount + " in robbery. ")
    print(" Next morning he filed complaint in " + robbery_location + " police station.")


def story_4() :
    king_name = input("Please enter a king name: ")
    number_of_queens = input("Please enter number of queens: ")
    child_name = input("Please enter a child name: ")
    king_place = input("Please enter a location: ")

    print("KING STORY")
    print("There was a king named " + king_name + ", ")
    print("he was having " + number_of_queens + " queen. ")
    print("he lived in" + king_place + ".")
    print("His child name is  " + child_name + ", ")
    print(" and they were living peacefully.")

def story_5() :
    character_name = input("Please enter a character name: ")
    favourite_food = input("Please enter your favourite food: ")
    vacation_place = input("Please enter a vacation place: ")
    weather_condition = input("Please enter weather condition : ")

    print("VACATION STORY")
    print("My name is " + character_name + ", ")
    print("I went to " + vacation_place + " on my last vacation. ")
    print("I ate " + favourite_food + " over there.")
    print("The weather was " + weather_condition + ". ")
    print(" I really enjoyed my vacation.")


def ending() :
    print()
    print("That was a good story!")
    
def key() :
    sum_bs = False
    
    
    fable_type = random.randint(1, 5) 
    print()

    if fable_type > 5:
        print("story limit exceeded")
        sum_bs = True
    elif fable_type == 1:
        story_1()
        #ending()
    elif fable_type == 2:
        story_2()
        #ending()
    elif fable_type == 3:
        story_3()
        #ending()
    elif fable_type == 4:
        story_4()
        #ending()
    elif fable_type == 5:
        story_5()
        #ending()    

    if sum_bs == False:
        ending()

key()
