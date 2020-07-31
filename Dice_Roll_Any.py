# Name    : Dice_Roll_Any.py
# Author  : Samuel Lamb
# Purpose : Software to emulate rolling a dice, allowing for any size dice to be selected
import random

def Roll(x):
  Quantity = int(input("How many do you want to roll?: "))
  Quantity = abs(Quantity)
  Score = 0
  while(Quantity != 0):
    randRoll = random.randint(1,x)
    Quantity = Quantity - 1
    print("You rolled:",randRoll)
    Score += randRoll
  return Score

while(True):
  Result = 0
  Sides = int(input("Please enter number of sides (Enter 0 to leave): ")) # User enters an integer value for number os sides of dice
  Sides = abs(Sides)
  if (Sides == 0): # If 0 is entered, exit program
    print("Thank you! Good luck")
    break 
  Result = Roll(Sides)
  print("Your score is: ",Result)