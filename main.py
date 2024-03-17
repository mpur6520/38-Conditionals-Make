#Maru Puran
#October 23, 2023
#Create a grade tester program to utilize if else and else if and else statements inside a program to understand how they can be used in programs and what utility they provide, such as allowing the computer to output code based on choices 

#regular code:

grade = int(input("Please enter a test grade between 1 and 100, inclusive: ")) #ask user to enter a grade between 1 and 100 and store it as an integer in the variable grade

if grade < 1 or grade > 100: #check if the number is valid; if it's between 1 and 100 inclusive
    print("That is not a valid grade. Please restart and enter a grade between 1 and 100.") #if the conditional is false (the grade isn't valid) print that, and alert the user

if grade < 40: #check if the grade is below a 40
  fail = "Y" #set variable fail to Y meaning the user has failed
elif grade >= 40: #check if the grade is greater than or equal to 40
  fail = "N" #set variable fail to N meaning the user hasn't failed

if fail != "N": #check if the variable fail is NOT equal to N
  print("You should retake your test! That's really low.") #print the words retake required if conditional is true
else:
  print("Congraulations on passing, you've passed with over a 40!")

input("\nAccording to your grade, what letter grade do you think you got?: ")

#extra challenge:

if grade >= 80: #check if the grade is greater than or equal to 80
  print("\nYou've gotten an A grade. Nice work!") #print the user has gotten an A grade if conditional true
elif grade <= 79 and grade >= 69: #check if grade is greater than or equal to 69 but also less than or equal to 79
  print("\nYou've gotten a B grade. Good job!") #if true print the user has gotten a B grade
elif grade <= 68 and grade >= 40: #check if grade is greater than or equal to 40 but also less than or equal to 68
  print("\nYou've gotten a C grade. Maybe study some more!") #if true print the user has gotten a C grade
elif grade < 40: #check if grade is less than 40
  print("\nYou've gotten a U grade.. sorry!") #if true print the user has gotten a U grade
else: #if none of conditionals are true run this code
  print("\nThe program doesn't have an answer for you.") #alert the user that the program doesn't have an answer for them
  