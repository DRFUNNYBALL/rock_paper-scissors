import random
import colorama
from colorama import Style,Back,Fore,init
init()

print(Fore.LIGHTCYAN_EX +"ROCK____PAPER____SCISSORS")

user = input(Fore.LIGHTMAGENTA_EX + "please return your choise :")
number=random.randint(1,3)
Robot=""

if number== 1:
    player=("ROCK")
    print("Robot choise ROCK")
elif number==2:
    player=("PAPER")
    print("Robot choise PAPER")
elif number==3:
      player=("SCISSORS")
      print("Robot choise SCISSORS")

if   player=="ROCK" and user=="PAPER":
      print(Fore.GREEN + "YOU WIN")
elif player=="ROCK" and user=="SCISSORS":
      print(Fore.RED +"YOU LOSE")
elif  player=="PAPER" and user=="SCISSORS":
      print(Fore.GREEN +"YOU WIN")
elif player=="PAPER" and user=="ROCK":
      print(Fore.RED +"YOU LOSE")
elif player=="SCISSORS" and user=="PAPER":
      print(Fore.RED +"YOU LOSE")
elif player=="SCISSORS" and user=="ROCK":
      print(Fore.GREEN +"YOU WIN")
elif player=="SCISSORS" and user=="SCISSORS":
      print(Fore.LIGHTMAGENTA_EX+"equls!!!")
elif player=="ROCK" and user=="ROCK":
      print(Fore.LIGHTMAGENTA_EX+"equls!!!")
elif player=="PAPER" and user=="PAPER":
      print(Fore.LIGHTMAGENTA_EX+"equls!!!")
else:
      print(Fore.LIGHTRED_EX + "wrong choise")

