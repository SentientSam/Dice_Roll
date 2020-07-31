# Name    : Dice_Roll.py
# Author  : Samuel Lamb
# Purpose : Software to emulate rolling a dice, allowing for any size dice to be selected
import random

validEntry = False
Result = 0
while(True):
  Roll = int(input("Please enter number of sides (Enter 0 to leave): "))

  if (Roll == 10):
      validEntry = True
      randRoll = random.randint(0,9)
      percentRoll = random.randrange(00,90,10)
      print("You rolled:",percentRoll,"and:",randRoll)
      if (randRoll == 0 and percentRoll == 0):
        Result = 100
      else:
        Result = randRoll + percentRoll
  if (Roll == 0):
    validEntry = True
    print("Thank you! Good luck")
    break
  if (Roll != 10 and validEntry == True):
    Quantity = int(input("How many do you want to roll?: "))

  if (Roll == 8):
    validEntry = True
    while(Quantity != 0):
      randRoll = random.randint(1,8)
      Quantity = Quantity - 1
      print("You rolled:",randRoll)
      Result += randRoll

  if (Roll == 6):
    validEntry = True
    while(Quantity != 0):
      randRoll = random.randint(1,6)
      Quantity = Quantity - 1
      print("You rolled:",randRoll)
      Result += randRoll

  if (Roll == 4):
    validEntry = True
    while(Quantity != 0):
      randRoll = random.randint(1,4)
      Quantity = Quantity - 1
      print("You rolled:",randRoll)
      Result += randRoll

  if (Roll == 20):
    validEntry = True
    while(Quantity != 0):
      randRoll = random.randint(1,20)
      Quantity = Quantity - 1
      print("You rolled:",randRoll)
      Result += randRoll

  if (Roll == 12):
    validEntry = True
    while(Quantity != 0):
      randRoll = random.randint(1,12)
      Quantity = Quantity - 1
      print("You rolled:",randRoll)
      Result += randRoll    
  if(validEntry == False):
    print("That type of dice is not supported or does not exist, please try again!")

  if(Roll == 10):
    print("Your score is: ",Result,"%")
    validEntry == False
  else:
    if(validEntry == True):
      print("Your score is: ",Result)
      validEntry == False
