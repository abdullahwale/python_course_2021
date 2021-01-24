print(''' 
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')

print("Welcome Into treasure ILand Game")
print("Your Mission is to Find Treasure")
choice1=input("You can see two Side 'left' or 'right' ").lower()

if choice1=='left':
  choice2=input("You have two Options 'swim' or 'wait' ").lower()
  if choice2== 'wait':
    choice3=input("You have three Doors 'yellow' or 'green' or 'blue' ").lower()
    if choice3=='yellow':
      print("You won the Game")
    else:
      print("Game Over")
  else:
   print("Game Over")  

else:
  print("Game Over")
