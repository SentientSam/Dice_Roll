# Name    : Dice_Roll.py
# Author  : Samuel Lamb
# Purpose : Software to emulate rolling a dice, allowing for any size dice to be selected
import random

validEntry = False # Variable to check for a valid (or supported) dice

while(True):

  Result = 0

  Sides = int(input("Please enter number of sides (Enter 0 to leave): ")) # User enters an integer value for number os sides of dice

  if (Sides == 10): # For use with DnD, if they are rolling a d10 then it is a percentage roll consisting of two dice
      validEntry = True
      randRoll = random.randint(0,9)
      percentRoll = random.randrange(00,90,10)
      print("You rolled:",percentRoll,"and:",randRoll)
      if (randRoll == 0 and percentRoll == 0):
        Result = 100
      else:
        Result = randRoll + percentRoll

  if (Sides == 0): # If 0 is entered, exit program and flag validEntry so that the score is not posted
    validEntry = True
    print("Thank you! Good luck")
    break

  if (Sides != 10 and validEntry == True): # If valid entry (and not the percentile dice), ask how many dice they want to roll
    Quantity = int(input("How many do you want to roll?: "))

  if (Sides == 8):
    validEntry = True
    while(Quantity != 0):
      randRoll = random.randint(1,8)
      Quantity = Quantity - 1
      print("You rolled:",randRoll)
      Result += randRoll

  if (Sides == 6):
    validEntry = True
    while(Quantity != 0):
      randRoll = random.randint(1,6)
      Quantity = Quantity - 1
      print("You rolled:",randRoll)
      Result += randRoll

  if (Sides == 4):
    validEntry = True
    while(Quantity != 0):
      randRoll = random.randint(1,4)
      Quantity = Quantity - 1
      print("You rolled:",randRoll)
      Result += randRoll

  if (Sides == 20):
    validEntry = True
    while(Quantity != 0):
      randRoll = random.randint(1,20)
      Quantity = Quantity - 1
      print("You rolled:",randRoll)
      Result += randRoll

  if (Sides == 12):
    validEntry = True
    while(Quantity != 0):
      randRoll = random.randint(1,12)
      Quantity = Quantity - 1
      print("You rolled:",randRoll)
      Result += randRoll    

  if(validEntry == False): # If not valid entry, repeat loop but inform user that the type of dice they entered is not supported
    print("That type of dice is not supported or does not exist, please try again!")

  if(Sides == 10): # If a d10, the result will be a percentile
    print("Your score is: ",Result,"%")
    validEntry == False

  else:
    if(validEntry == True): 
      print("Your score is: ",Result)
      validEntry == False
