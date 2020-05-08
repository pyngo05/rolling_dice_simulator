import random

cmd = ''
while True:
    cmd = input("Press y to roll die or q to quit: ")
    if cmd.lower() == 'y':
        print("You rolled a " + str(random.randrange(1, 7)))
    elif cmd.lower() == 'q':
        break
