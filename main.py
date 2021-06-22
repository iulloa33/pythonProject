#This is the base code for a small text game. It takes place in a labryinth and your goal is to escape.
from colorama import Fore, Back, Style

print(Back.BLACK + 'WELCOME TO THE', end = " ")
print(Fore.RED + "LABYRINTH")

print("You are trapped within the great labyrinth. Test your knowledge and skill to escape!!!")

print("")
print(Fore.YELLOW + "Before you are 3 doors. The first has a skull, the second a Sword, and the third a Bow. Choose by typing 1, 2, or 3.")

choice = input("Choose Wisely: ")

if choice == '1':
    print(Fore.RED + "You enter the first door only to fall to your demise!")
    exit()
elif choice == '2':
    print(Fore.BLUE + "You enter the 2nd door and find an empty room with a podium in its center. Upon the podium is a sword. "
                       "You carefully take the sword.")
    weapon = "sword"
elif choice == '2':
    print(Fore.BLUE + "You enter the 2nd door and find an empty room with a podium in its center. Upon the podium is a bow. "
                       "You carefully take the bow.")
    weapon = "bow"

print("")

print(Fore.YELLOW + "Once again 3 doors face you. Upon the first are many figures of small creatures, upon the second a snake, and the third a golem.")
choice = input("Choose Wisely: ")

print("")

if choice == '1':
    print(Fore.GREEN + "You walk into 1st room to find 4 goblins facing you in the distance.")
    print("             ,      ,              ,      ,             ,      ,             ,      ,")
    print('            /(.-""-.)\            /(.-""-.)\           /(.-""-.)\           /(.-""-.)\\')
    print('        |\  \/      \/  /|    |\  \/      \/  /|   |\  \/      \/  /|   |\  \/      \/  /|')
    print('        | \ / =.  .= \ / |    | \ / =.  .= \ / |   | \ / =.  .= \ / |   | \ / =.  .= \ / |')
    print('        \( \   o\/o   / )/    \( \   o\/o   / )/   \( \   o\/o   / )/   \( \   o\/o   / )/')
    print("         \_, '-/  \-' ,_/      \_, '-/  \-' ,_/     \_, '-/  \-' ,_/     \_, '-/  \-' ,_/")
    print('           /   \__/   \          /   \__/   \         /   \__/   \         /   \__/   \\')
    print("           \ \__/\__/ /          \ \__/\__/ /         \ \__/\__/ /         \ \__/\__/ /")
    print("         ___\ \|--|/ /___      ___\ \|--|/ /___     ___\ \|--|/ /___     ___\ \|--|/ /___")
    print('       /`    \      /    `\  /`    \      /    `\ /`    \      /    `\ /`    \      /    `\\')
    print("      /       '----'       \/       '----'       /       '----'       /       '----'       \\")

    print('')
    if weapon == "sword":
        print(Fore.YELLOW + "With your sword in hand you rush the goblins but quickly find they're are too many to fight at this range!")
        print(Fore.RED + "You fight your hardest, but this is where you find your END")
        exit()
    elif weapon == "bow":
        print(Fore.YELLOW + "The goblins try to rush you; however with your bow you manage to dispatch them 1 by 1 before they can reach you!")

elif choice == '2':
    print(Fore.GREEN + "You walk into the 1st room to find a giant serpent facing you in the distance.")
    print("             ____")
    print("            / . .\\")
    print("            \  ---<      i'm big boi >:(")
    print("             \  /")
    print("   __________/ /")
    print("-=:___________/")

    print('')
    if weapon == "sword":
        print(Fore.YELLOW + "With your sword you rush towards the serpent, quickly defeating the serpent with your strength")
    elif weapon == "bow":
        print(Fore.YELLOW + "You shoot your arrows at the serpent; however, the arrows bounce off its strong scales.")
        print(Fore.RED + "You fight your hardest, but this is where you find your END")
        exit()

elif choice == '3':
    print(Fore.RED + "You enter the third door to find a Golem towering over you.")
    print("In this instant you know your weapon will be of no use against the tough stone on its surface.")
    print(Fore.RED + "You fight your hardest, but this is where you find your END")
    exit()

print('')
print(Fore.BLUE + "Before you is a blue door. You open it to find yourself in the middle of dense forest.")
print("The door you came from is nowhere to be seen, but you know you are free of the Labyrinth.")
print('As you begin to walk away you hear a whisper "Till the labyrinth seeks you again young warrior"')
