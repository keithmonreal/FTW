# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 00:15:37 2020

@author: Keith Monreal
"""

# Give the user some context and get his or her name
print("\nAre you ready to take a quiz about everything and anything under the sun?")
choice = input("Yes or No\n")

if 'Yes' in str(choice):
   print("\nOkay, let's do this!.  But first, what is your name?")
else:
  print("\nOkay, whenever you're ready.")

name = input("Please input your beautiful name here:\n")

print("\nHi" + " " + str(name) + " " + "!" + " " + "Here is your first question.")

#set questions
questions = ["A sneeze is faster than an eye blink",
            "Olympic gold medal is made of silver",
            "Chocolate is lethal to dogs.",
            "Shrimp's heart is in its head.",
            "Pigs cannot look up into the sky.",
            "Fingernails grow faster than hair",
            "A shark can blink its eyes",
            "Snoopy is yellow in Brazil.",
            "Gorilla's blood type is all B",
            "Sandwich is named after a person."]

#set the right answers
right_answers = ["T","T","T","T","T","F","T","F","T","T"]

#initialize the variables that will be used
answers = []
question_number = 0
score = 0

#last_question
def last_question(answers,score):
      print("Your answers are" + " " + str(answers)) 
      score = score/10
      if score > 0.60:
        print("Congratulations! You passed!")
      else:
        print("You failed. It's okay, they are useless facts anyway.")
      score = "{:.2%}".format(score)
      print("\nYour score is" + " " + str(score))
  
#while loop for the question proper
while question_number < 10:
    print("\n" + str(questions[question_number]))
    answer_n = input("\nT or F \n")
    answers.append(answer_n)
    if answers[question_number] == right_answers[question_number]:
       score = score + 1
    question_number = question_number + 1
    if question_number == 10:
      last_question(answers,score)