from Ui import Gui, Terminal
from sys import argv

def usage():   
    print(f"""
Usage: {argv[0]} [g | t]
g : Play with the Gui
t : Play with the Terminal""")
    quit()

# Added a comment
if __name__ == "__main__":
    if len(argv) != 2:
        usage()
    elif argv[1] == 't':
        ui = Terminal()
    elif argv[1] == 'g':
        ui = Gui()
    else:
        usage()

    # Polymorphism being used
    ui.run()
