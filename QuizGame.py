#)You are required to design, implement and test a small console-based quiz in Python which performs the description given below.

#)The quiz should ask the user(s) 10 questions. The quiz topic can be 
#)on any subject of your choice.

#)You are required to produce a program which reads in, from the console 
#)(command line), ten quiz questions and ten correct answers, one correct answer for each question.




#)Once you have added these questions to your program, you then need to 
#)extend the console (command line) interface so that it:




#2)Asks the user their name

username = input("Enter username:")
print("Username is: " + username)



#Runs through all questions of the quiz and keep a running 
#score of the number of correctly questions answered;

#)Once the users has answered all the questions, the system should print out their score out of 10 as well as a percentage score on the screen;
#)The program should then prompt to ask if anybody else wants to take the quiz. It should then perform steps 1-4 again for the next user;
#)Once all the users have finished the quiz, the program displays:
#)The name of the user with the highest score (as well as other users’ score).
#)The average score of all users.
#)You should make use of conditional statements, iterative statements, py, data structures etc. in your program.
#)Your program should suitably handle user errors (e.g., incorrect input type, such as empty answer or name etc.).
#)The above describes the basic features that you are expected to attempt for this assessment. Extra marks are available if you can extend your program so that it implements the following additional features:

#)You can produce a quiz which can ask any number of questions (i.e. user can specify the number of questions they wan to answer, e.g., 15 questions).
#)The system displays questions in random order each time the quiz is taken.
#)The user is shown which questions they got correct and which they got incorrect (as well as showing the correct answer for any questions they answered incorrectly
#)Your source code should include sufficient and correctly formatted comments. 





















#!/usr/bin/env python3


import time



a = 10
b = 20
print(a+b)

#https://codereview.stackexchange.com/questions/153495/simple-multiple-choice-quiz


questions = ["How much floor space did the ENIAC computer, unveiled in 1946, take up?",
             "What was the first commercially produced computer?",
             "In what year was the first e-mail sent?",
             "Who designed the Apple I?",
             "What video game did the Apple II come with?",
             "What was the first portable computer?",
             "What's the best-selling computer model of all time?",
             "What was the first computer with graphical user interface?",
             "Who designed the Linux operating system?",
             "What was the original name of Yahoo when the company was founded in 1994?"]



answer_choices = ["a)1000 square feet\n b)200 square feet\n c)3000 square feet \n d) 400 square feet \n:",
                  "a)Osborne 1\n b)ERA 1101\n c)Intel Pentium 3 \n d) C64\n:",
                  "a)1999\n b)1972\n c)1984\n d)1971\n:",
                  "a)ERA 1101\n b)Osborne 1\n c)Intel Pentium 3 \n d) C64\n:",
                  "a)ERA 1101\n b)Osborne 1\n c)Intel Pentium 3 \n d) C64\n:",
                  
                  
                  
                  "a)1967\nb)1955\nc)1987\nd)1994\n:"]


correct_choices = ["a","b","d"]

options = ["a","b","c","d"]

answers = ["1,000 square feet",
           "ERA 1101",
           "1971",
           "Steve Wozniak",
           "Breakout",
           "Osborne I",
           "Commodore 64",
           "Apple Lisa",
           "Linus Torvalds",
           "Jerry'sGuide to the World Wide Web"]


def quiz():
    start = time.time()
    #store user score into a variable
    score = 0
    
    
    #assign a variable for questions, answer_choice, correct_choices, answers
    #combine each of of the list eg:
    
    #question + answer + correct answer + answerfromsystem
    
    
    
    for question, choices, correct_choice, answer in zip(questions, answer_choices, correct_choices, answers):
        #system prompt question to user
        print(question)
        #user input answer
        user_answer = input(choices).lower()
               
        #check if user in put match any options, loop until user will give one of the correct options
        while user_answer not in options:
            print("please select only on of the given options.eg:a,b,c,d")
            user_answer = input(choices).lower()
         
         
         
        #if instead user input is correct (as its one of the given options) brake the loop and go to next step
        else:
            #if user input is in one of the correct options then prompt(Correct Answer)
            if user_answer in correct_choice:
            #prompt to user that the answer is correct
                print("****Well Done!!! Answer is Correct****")
            #prompt score to user
                score += 1
            ######################################################U ARE HERE ########################
            # if answer doesnt exist in assigned correct choices
            else:
                print("****Answer is Incorrect****","The correct answer is:", answer)   

            
        
        #scan user answer (as a string) and check if the it exists in the assigned correct_choice variable
        
        
        
    print("You've finished the game...let's check your results!")
    
    elapsed = time.time()
    
    print("Elapsed time:",elapsed - start)
    
    print("****Your Score****")
    print(score, "out of", len(questions),"correct answers")
    print("Your score is:", float(score / len(questions)) * 100, "%")



if __name__ == "__main__":
   quiz()
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    