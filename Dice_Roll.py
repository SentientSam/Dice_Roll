# Name    : Dice_Roll.py
# Author  : Samuel Lamb
# Purpose : Software to emulate rolling a dice, allowing for any size dice to be selected
import random

validEntry = False # Variable to check for a valid (or supported) dice

while(True):

  Result = 0
  
  Sides = int(input("Please enter number of sides (Enter 0 to leave): ")) # User enters an integer value and 

  if (Sides == 10):
      validEntry = True
      randRoll = random.randint(0,9)
      percentRoll = random.randrange(00,90,10)
      print("You rolled:",percentRoll,"and:",randRoll)
      if (randRoll == 0 and percentRoll == 0):
        Result = 100
      else:
        Result = randRoll + percentRoll

  if (Sides == 0):
    validEntry = True
    print("Thank you! Good luck")
    break

  if (Sides != 10 and validEntry == True):
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

  if(validEntry == False):
    print("That type of dice is not supported or does not exist, please try again!")

  if(Sides == 10):
    print("Your score is: ",Result,"%")
    validEntry == False

  else:
    if(validEntry == True):
      print("Your score is: ",Result)
      validEntry == False
