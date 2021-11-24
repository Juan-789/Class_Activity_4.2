"""
2. Write a program that takes from the user a number and prints Xs horizontally
"""
numHorizontal = int(input("How many times do you want me to iterate 'X' horizonatally? "))\
#Prints numHorizontal times "X" horizontally.
for i in range(numHorizontal):
  print("x", end = " ")
#Separates each iteration of "X" with a " ".