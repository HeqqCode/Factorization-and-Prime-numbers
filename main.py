import random
import sys

#The code is very inneficient cause binary trees suck
#vars/lists & error handling

while True:

  try:
    n = int(input("Enter a number"))
  except ValueError:
    print("Number indentified as a non-integer. Please run the program again cause i dont want to put this in a loop just for you to be able to trick me again")
    break
  
  
  
  
  
  def getANumb():
    a = sys.maxsize # largest possible integer mate
    return random.randint(0,a)
  
  factors = []
  def factorize(): # thanks chatgpt for the algo.. idk if the code is effifient
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:  
                factors.append(n // i)
    return sorted(factors)
  
  
  print(factorize())  # Output: [1, 2, 4, 7, 14, 28]
  
  #check if it is a prime without function lol
  if factors == [1,n]:
    print("It is prime")
    print("logan paul and ksi be trippin with numbers")
  
  
  #print(getANumb())
  
  
