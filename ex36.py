from sys import exit

def start():
    print("You find yourself in a dark room.")
    print("You feel around and find something cool and round.")
    print("You continue looking around, and find two more such objects.")
    print("""As your eyes adjust to the darkness, you realize you are in a room
    with three doors.""")
    print("Which door would you like to open? \n1\n2\nor 3?")
    choice = input("> ")

    if choice == "1":
        print("You open the door and are blinded by a bright light.")
        outside()
    elif choice == "2":
        print("You open the middle door, and are led in to a dimly lit tunnel leading downwards.")
    elif choice == "3":
        print("You open the last door. It squeaks terribly as you pry it open.")
        print("You smell something rancid, yet can see less than in the previous room.")
    else:
        print("You remain in place and ponder your predicament.")

def outside():
    print("You have made it outside. There is a cool breeze.")
    print("You see a large man coming toward you with a bristly beard. He is ginormous.")
    print("He glares at you with beady black eyes.")
    print("Do what would you like to do?")
    print("1. Run back inside.\n2. Charge the beady eyed man\n3. Stand in place.")
    choice = input("> ")

    if choice == "1":
        print("You run back inside like a massive weakling.")
    elif choice == "2":
        print("The beady eyed man screeches loudly!")
    elif choice == "3":
        print("The man approaches and says he comes in peace.")
    else:
        print("The man is still approaching...")
        outside()

start()
