# Author:Dario Florio
# Date:29-08-2022
#!/usr/bin/env python3
###################################################### DEPENDECIES ########################
# import modules/dependencies
import time
import datetime
import random
from data import questions, answers, correct_choices, answers, options, scores

###################################################### DEPENDECIES ########################

###################################################### METHODS ############################


#######----------------------------------------#######
# GREETING METHOD
# this method take take one argument:name 
# it will prompt a greeting  based on the time of the day
# it uses the time module
# name:string
def greetings(name):
    currentTime = datetime.datetime.now()   
    currentTime.hour
    if currentTime.hour < 12:
        print('< Good morning', name, "/>")
    elif 12 <= currentTime.hour < 18:
        print('< Good afternoon', name, "/>")
    else:
        print('< Good evening', name, "/>")
#######----------------------------------------#######

    
#######----------------------------------------#######
# quiz METHOD
# this method take take four arguments:name, questions,answers, correct_choices 
# name:string
# questions:list
# answers:list
# correct_choices:list        
def quiz(name, questions, answers, correct_choices): 
    # store user score into a variable
    score = 0 
    # grab data from lists in datafile
    temp = list(zip(questions, answers, correct_choices))
    # shuffle questions
    random.shuffle(temp)
    # combine lists eg. question-answer
    questions, answers, correct_choices = zip(*temp)
    # create a list in which to append user's wrong answers
    wrong_answers = []

    for question, answer, correct_choices in zip(questions, answers, correct_choices):
        # system prompt question to user
        print(question)
        print("(Please choose a,b,c,d)")
        # user input answer
        user_answer = input(answer).lower()               
        # check if user in put match any options, loop until user will give one of the correct options
        while user_answer not in options:
            print("please select only on of the given options.eg:a,b,c,d")
            user_answer = input(answer).lower()
        # if instead user input is correct (as its one of the given options) brake the loop and go to next step
        else:
            # if user input is in one of the correct options then prompt(Correct Answer)
            if user_answer in correct_choices:
            # add 1 point to score
                score += 1           
            # if answer doesnt exist in assigned correct choices
            else:
                wrong_answers.append(question)            
     # Game finish, display stats
    print("Great Work", name, "You've finished the game!")    
    print("****Your Score****")
    print(score, "out of", len(questions), "correct answers")
    print("Your score is:", float(score / len(questions)) * 100, "%")   
    print("************************Scoreboard************************")
    
    #######----------------------------------------DISPLAY SCORES#######  
    # Update Users score
    scores.update({name: score})
    # sort dictionary values in descending order
    scoreboard = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    # iterate through the given tuple to display scores
    for name, score in scoreboard:
        print(name, score)
                
    #######----------------------------------------DISPLAY AVERAGES####### 
    # loop to sum all values 
    res = 0
    for val in scores.values():
        res += val
    # using len() to get total keys for mean computation
    res = res / len(scores) 
    # printing result 
    print("The average score is : " + str(res)) 
 
    print("**********************************************************") 
 #######----------------------------------------#######        


# again METHOD
# this method prompt the question, do you want to play again?
# It will only accept a Y or N answer to proceed into the next step
# If the user will answer Y, then the program will restart the game
#######----------------------------------------#######  
def again():
    if input("Does anybody else wants to take the quiz?.Enter y to continue or press anything else to quit\n") == 'y':
        game()
    else:
        exit
#######----------------------------------------#######                

    
# game METHOD
# this method prompt the user with the game
# it will force the use user to input his name
#######----------------------------------------#######        
def game(): 
    start = time.time()     
# Ask for user name
# if user press enter and gives blank input then repeat the question
    while True:
        name = input("<Please enter your name to start the game:/> \n")
        if name:
            print("  ")
        # import greeting method
            greetings(name)
            print("  ")           
            quiz(name, questions, answers, correct_choices)       
            break
   
    elapsed = time.time()
    print("Elapsed time:", elapsed - start)
    print("**********************************************************")  
    again() 
#######----------------------------------------####### 
    
###################################################### METHODS ########################

