import random
from turtle import *
import time
import datetime
import webbrowser
import math
def binary_converter(string):
    for character in string:
        print(bin(ord(character))[2:].zfill(8))
R_P_S = 0
def square(number):
    print(number * number)
eight_ball = 0
equation = 0
wrong = 0
website = 0
talk = 0
class_school = 0
alarm = 0
timer_name = 0
time_pass = 0
player_choice = 0
query = 0
timer = 0
b = 0
name = "(put your name here)"
now = datetime.datetime.now()
print(f"hello {name}")
command = input(f"Do you want to 1.make me say something 2.tell me the date 3.set a alarm 4.set a timer 5.flip a coin 6.do math 7.play Rock, paper, scissor(RPS) 8.search something up 9.tell me a joke 10.ask the magic 8 ball something 12.tell me a riddle 13. roll a dice 14.convert english to binary 15.other projects best gamer5950 did: ")
while True:
#commands
    if command == "say something":
        break
    elif command == "hello there" or command == "HELLO THERE":
        print("GENERAL KENOBI")
        break
    elif command == "best gamer" or command == "bestgamer" or command == "bestgamer 5950" or command == "best gamer 5950" or command == "bestgamer5950" or command == "best gamer5950" or command == "projects" or command == "project":
        break
    elif command == "riddle" or command == "tell me a riddle":
        break
    elif command == "date" or command == "time":  
        break
    elif command == "dice" or command == "roll a dice":
        break
    elif command == "binary" or command == "converter to binary":
        break
    elif command == "alarm":
        break
    elif command == "timer" or command == "set a timer":
        timer = input("do you want to set in hour, min, or secs: ")
        timer_name = input("Do you want to name the timer: ")
        break
    elif command == "flip a coin" or command == "coin":
        break
    elif command == "what is a good music":
        print("billy joel or any type of rock")
    elif command == "math" or command == "do math":
        equation = input("do you want to add, subtract, multiply, or divide: ")
        break
    elif command == "rock paper scissor" or command == "RPS" or command == "rps":
        player_choice = input("what do you chose rock, paper, or scissors: ")
        break
    elif command == "search" or command == "search something":
        query = input("what do you want to search(may take a while): ")
        number_search = int(input("how much websites do you want to search: "))
        break
    elif command == "hi":
        print(f"hello {name} my name is sori")
        break
    elif command == "tell me a joke" or command == "tell a joke":
        break
    elif command == "ask the magic 8 ball" or command == "8 ball" or command == "ask the magic 8 ball something":
        break
    else:
        print("sorry you might of type the command wrong try again")
        time.sleep(2)
        command = input("Do you want to 1.open a website 2.make me say something 3.tell me the date 4.set a alarm 5.set a timer 6.flip a coin 7.do math 8.play Rock, paper, scissor(RPS) 9.search something up 10.tell me a joke 11.tell me my class schedule 12.ask the magic 8 ball something: ")


#timer
time = 0
if command == "timer" or command == "set a timer":
    if timer_name == "no":
        timer_name = "timer done"
    elif timer_name == "yes":
        timer_name = input("what do you want to name it: ")
    if timer == "hour":
        timer = int(input("how many hours: "))
        timer = timer * 3600
    if timer == "min":
        timer = int(input("how many min: "))
        timer = timer * 60
    if timer == "sec":
        timer = int(input("how many sec: "))
    while True:
        time.sleep(1)
        time_pass += 1
        if timer == time_pass:
            print(f"{timer_name}")
            pen = turtle.Turtle()
            pen.write(f"{timer_name}", font=("Calibri", 15, "bold"))

#do math
if equation == "add":
    number = int(input("what is the first number: "))
    number_1 = int(input("what is the secound number: "))
    answer = number + number_1
    print(f"{answer}")
if equation == "subtract":
    number = int(input("what is the first number: "))
    number_1 = int(input("what is the secound number: "))
    answer = number - number_1
    print(f"{answer}")
if equation == "multiply":
    number = int(input("what is the first number: "))
    number_1 = int(input("what is the secound number: "))
    answer = number * number_1
    print(f"{answer}")
if equation == "divide":
    number = int(input("what is the first number: "))
    number_1 = int(input("what is the secound number: "))
    if number == 0 and number_1 == 0:
        print("ERROR a idiot is using me")
    elif number != 0 and number_1 != 0:
        answer = number / number_1
        print(f"{answer}")

#Rock paper scissors
R_P_S = random.randint(1,3)
if R_P_S == 1:
    R_P_S = "rock"
elif R_P_S == 2:
    R_P_S = "paper"
elif R_P_S == 3:
    R_P_S = "scissors"
if player_choice == "rock" and R_P_S == "rock":
    print("It's a tie")
elif player_choice == "rock" and R_P_S == "paper":
    print("you lose")
elif player_choice == "rock" and R_P_S == "scissors":
    print("you win")
elif player_choice == "paper" and R_P_S == "rock":
    print("you win")
elif player_choice == "paper" and R_P_S == "paper":
    print("it's a tie")
elif player_choice == "paper" and R_P_S == "scissors":
    print("you lose")
elif player_choice == "scissors" and R_P_S == "rock":
    print("you lose")
elif player_choice == "scissors" and R_P_S == "paper":
    print("you win")
elif player_choice == "scissors" and R_P_S == "scissors":
    print("it's a tie")

#search things
if command == "search" or command == "search something":
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
  
    # to search
    for j in search(query, tld="co.in", num=number_search, stop=number_search): 
        print(j)
        webbrowser.open_new_tab(f"{j}")

#riddles
if command == "riddle" or command == "tell me a riddle":
    riddle = random.randint(1,12)
    if riddle == 1:
        riddle = input("I’m tall when I’m young and I’m short when I’m old. What am I? ")
        if riddle == "candle" or riddle == "a candle":
            print("good job you did it")
        else:
            print("wrong answer it was candle")
    if riddle == 2:
        riddle = input("Where can you find cities, towns, shops, and streets but no people? ")
        if riddle == "a map" or riddle == "map":
            print("good job you did it")
        else:
            print("wrong answer it was a map")
    if riddle == 3:
        riddle = input("What five letter word becomes shorter when you add two letters to it? ")
        if riddle == "shorter" or riddle == "short":
            print("good job you did it")
        else:
            print("wrong answer it was shorter")
    if riddle == 4:
        riddle = input("What is so fragile that saying its name breaks it? ")
        if riddle == "silence":
            print("good job you did it")
        else:
            print("wrong answer it was silence")
    if riddle == 5:
        riddle = input("What word is spelled wrong in every dictionary? ")
        if riddle == "wrong":
            print("good job you did it")
        else:
            print("wrong answer the answer was wrong because it is the only word spelled wrong")
    if riddle == 6:
        riddle = input("I have no life, but I can die. What am I? ")
        if riddle == "battery" or riddle == "a battery":
            print("good job you did it")
        else:
            print("wrong answer the answer was battery")
    if riddle == 7:
        riddle = input("I have no life, but I can die. What am I? ")
        if riddle == "battery" or riddle == "a battery":
            print("good job you did it")
        else:
            print("wrong answer the answer was battery")
    if riddle == 8:
        riddle = input("What has 88 keys, but cannot open a single door? ")
        if riddle == "a piano" or riddle == "piano":
            print("goodjob you did it")
        else:
            print("wrong the answer was piano")
    if riddle == 9:
        riddle = input("Which weighs more: a pound of feathers or a pound of bricks? ")
        if riddle == "they weigh the same" or riddle == "both weigh the same":
            print("goodjob you did it")
        else:
            print("wrong the answer was they weigh the same because both weigh one pound")
    if riddle == 10:
        riddle = input("It belongs to you, but your friends use it more. What is it? ")
        if riddle == "name" or riddle == "your name":
            print("goodjob you did it")
        else:
            print("wrong the answer was your name")
    if riddle == 11:
        riddle == input("What gets bigger the more you take away? ")
        if riddle == "a hole" or riddle == "hole":
            print("goodjob you did it")
        else:
            print("wrong the answer was a hole")
    if riddle == 12:
        riddle == input("If you don't keep me, I break. What am I? ")
        if riddle == "a promise" or riddle == "promise":
            print("goodjob you did it")
        else:
            print("wrong the answer was a promise")
#dice roll
if command == "dice" or command == "roll a dice":
    dice_number = random.randint(1, 6)
    print(f"you rolled a {dice_number}")

#best gamer5950 projects
if command == "best gamer" or command == "bestgamer" or command == "bestgamer 5950" or command == "best gamer 5950" or command == "bestgamer5950" or command == "best gamer5950" or command == "projects" or command == "project":
    while True:
        project = input("which one; age predictor, movie(or or modded),turtle square, pets, or no name(couldn't think of anythink to name it), number quesser, square(math), draw a house: ")
        #age predictor
        if project == "age predictor":
        # Get the name from the user
            name = input("Enter your name: ")
        # Greet the user
            print(f"Hello {name}")
        # Get the age from the user
            age = input("How old are you?: ")
        # Calculate the age in 50 years
            future_age = 50 + int(age)
        # Tell the user how old they'll be in 50 years
            print(f"In 50 years you will be {future_age} years old.")
            break
        #movie
        elif project == "og movie" or project == "og":
            star_rating = int(input("Enter the star rating: "))
            genre = input("Enter the genre: ")
            good_genre = "sci-fi" == genre
            highly_rated = star_rating > 3
            if highly_rated == True and good_genre == True:
                print(f"yes this {genre} movie is a highly rated movie and this is a popular genre")

            elif highly_rated == True and good_genre == False:
                print(f"yes this {genre} movie is a highly rated movie but this is not a popular genre")

            elif highly_rated == False and good_genre ==True:
                print(f"no {genre} movie this is not a highly rated movie but this is a popular genre")

            elif highly_rated == False and good_genre ==False:
                print(f"no {genre} movie this is not a highly rated movie but this not is a popular genre")

            if highly_rated is True and good_genre is True:
                print("you should see this movie")
            break
#turtle
        elif project == "turtle" or project == "turtle square":
            size = int(input("Enter a size: "))

            turtle.pendown()

            turtle.forward(100 * (size))
            turtle.left(90)
            turtle.forward(100 * (size))
            turtle.left(90)
            turtle.forward(100 * (size))
            turtle.left(90)
            turtle.forward(100 * (size))
            turtle.left(90)


            turtle.mainloop()
            break
        #pets
        elif project == "pet" or project == "pets":
            animal = input("Enter your favorite pet (dog or cat): ")

            if animal == "dog":
                print("bark")

            if animal == "cat":
                print("Meow!")

            age = int(input("Enter the age of your pet: "))

            if age < 2:
                if animal == "dog":
                    print("Just a pup!")
                if animal == "cat":
                    print("Just a kitten!")
            elif age >= 8:
                print("your pet is kind of old")
            else:
                print("you pet is still young")
            break
        #no name
        elif project == "no name":
            number_1 = float(input("what is the first number: "))
            number_2 = float(input("what is the secound number: "))
            number_3 = float(input("what is the 3rd number: "))
            if number_1 > number_2:
                if number_1 > number_3:
                    print(f"{number_1} is greater then {number_2} and {number_3}")
                elif number_1 < number_3:
                    print(f"{number_3} is greater then {number_2} and {number_1}")
            elif number_1 < number_2:
                if number_2 > number_3:
                    print(f"{number_2} is greater then {number_1} and {number_3}")
                elif number_2 < number_3:
                    print(f"{number_3} is greater then {number_2} and {number_1}")
            else:
                print("all numbers are equal")
            break
#draw a house
        elif project == "house" or project == "draw a house":
            def draw_house(roof_color,base_color):
                color(base_color) 
                pendown()
                # Draw a 50 x 50 square
                for i in range(0, 4):
                    forward(50)
                    right(90)
                color(roof_color) 
                # Draw the triangle
                left(180)
                forward(10)
                right(135)
                forward(50)
                right(90)
                forward(50)
                right(135)
                forward(70)
                # Go to the starting point
                right(180)
                forward(10)

                penup()

            draw_house("red","blue")
            goto(100, 100)
            draw_house("green","purple")
            goto(200, 0)
            draw_house("pink","dark blue")
            goto(100, -100)
            draw_house("dark red","light blue")
            break

            #modded movie
        elif project == "modded" or project == "modded movie":
            while True:
                star_rating = int(input("Enter the star rating: "))
                if star_rating > 5:
                    print("inviled try again")
                    star_rating = int(input("Enter the star rating: "))
                elif star_rating <= 5:
                    break
                genre = input("Enter the genre: ")
                good_genre = "sci-fi" == genre
                highly_rated = star_rating > 3
                if highly_rated == True and good_genre == True:
                    print(f"yes this {genre} movie is a highly rated movie and this is a popular genre")

                elif highly_rated == True and good_genre == False:
                    print(f"yes this {genre} movie is a highly rated movie but this is not a popular genre")

                elif highly_rated == False and good_genre ==True:
                    print(f"no {genre} movie this is not a highly rated movie but this is a popular genre")

                elif highly_rated == False and good_genre ==False:
                    print(f"no {genre} movie this is not a highly rated movie but this not is a popular genre")

                if highly_rated is True and good_genre is True:
                    print("you should see this movie")
            break
        #number quesser
        elif project == "number" or project == "number quesser":
            secret_number = random.randint(1, 10)
            warm = [secret_number - 1, secret_number - 2, secret_number + 1, secret_number + 2]
            guessed_number = int(input("Guess a number between 1 and 10: "))
            while guessed_number != secret_number:
              if guessed_number in warm:
                print("getting warmer")
              else:
                print("getting colder")
              wrong = wrong + 1
              print("Nope! try again.")
              guessed_number = int(input("Guess a number between 1 and 10: "))
              if wrong == 4:
                print(f"you missed it five times you fail and the number was {secret_number}")
                break
            if guessed_number == secret_number:  
              print("You got it right!")
            break
        #square
        elif project == "square" or project == "square(math)":
            number = int(input("what number do you want to square: "))
            square(number)
            break
#binary converter
if command == "binary" or command == "converter to binary":
    binray_input = input("what do you want to say in binary: ")
    binary_converter(binray_input)
#say somthing
if command == "say something":
    talk = input("what would you like me to say: ")
    print(f"{talk}")
#time
if command == "date" or command == "time":  
    now = datetime.datetime.now()
    print(now.strftime("It's %A of %B %d %Y and it's %I:%M %p"))
#alarm
if command == "alarm":
    alarm = input("when do you want the alarm set too(put it in 24 hour style so like 08:50 AM): ")
    name_alarm = input("what do you want the alarm named: ")
    from datetime import datetime
    while True:
        now = datetime.now()
        dt_string = now.strftime("%H:%M %p")
        if alarm == dt_string:
            b += int(1)
            print(f"your alarm {name_alarm} is done")
        if b == 9:
            break
#flip a coin
if command == "flip a coin" or command == "coin":
    coin = random.randint(1,2)
    if coin == 1:
        print("It's tails")
    if coin == 2:
        print("It's heads")
#joke
if command == "tell me a joke" or command == "tell a joke":
    joke = random.randint(1,4)
    if joke == 1:
        print("your life")
    elif joke == 2:
        print("when i was created i had so many bugs")
    elif joke == 3:
        print("your mama is so fat she is the circus elephant")
    elif joke == 4:
        print("The person that made me didn't know how to do a basic If, Then statements")
#8 ball
if command == "ask the magic 8 ball" or command == "8 ball" or command == "ask the magic 8 ball something":
    eight_ball = random.randint(1,8)
    input("what do you want to ask: ")
    if eight_ball == 1:
        print("As I see it, yes.")
    elif eight_ball == 2:
        print("Ask again later.")
    elif eight_ball == 3:
        print("Better not tell you now.")
    elif eight_ball == 4:
        print("Cannot predict now.")
    elif eight_ball == 5:
        print("Concentrate and ask again.")
    elif eight_ball == 6:
        print("Don't count on it.")
    elif eight_ball == 7:
        print("It is certain.")
    elif eight_ball == 8:
        print("It is decidedly so.")
