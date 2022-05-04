from abc import ABC, abstractmethod
from Game import Game, GameError
from tkinter import Tk, Frame, Grid, N,S,E,W,Button, X, Y, Toplevel, StringVar, Scrollbar, Text, LEFT, RIGHT
from itertools import product
class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        root = Tk()
        root.title("Tic Tac Toe")
        frame = Frame(root)
        frame.pack()

        Button(
            frame,
            text="Help",
            command=self.__show_help
        ).pack(fill=X)

        Button(
            frame,
            text="Play",
            command=self.__play_game
        ).pack(fill=X)

        Button(
            frame,
            text="Quit",
            command=self.__quit
        ).pack(fill=X)

        scroll = Scrollbar(frame)
        console = Text(frame, height=4, width=50)
        scroll.pack(side=RIGHT, fill=Y)
        console.pack(side=LEFT, fill=Y)

        scroll.config(command=console.yview)
        console.config(yscrollcommand=scroll.set)

        self.__root = root

    def __show_help(self):
        pass

    def __play_game(self):
        self.__game = Game()

        game_win = Toplevel(self.__root)
        game_win.title("Game")
        frame = Frame(game_win)
        #frame.grid(row=0,column=0)

        # To allow resizing of the game window
        Grid.columnconfigure(game_win, 0, weight=1)
        Grid.rowconfigure(game_win, 0, weight=1)
        frame.grid(row=0,column=0,sticky=N + S + E + W)

        self.__buttons = [[None for _ in range(3)] for _ in range(3)]
        for row,col in product(range(3),range(3)):
            b = StringVar()
            b.set(self.__game.at(row+1,col+1))
            self.__buttons[row][col] = b

            cmd = lambda r=row, c=col: self.__play(r,c)

            Button(
                frame,
                textvariable=b,
                command=cmd
            ).grid(row=row,column=col,sticky=N+S+W+E)

        # To allow resizing
        for i in range(3):
            Grid.rowconfigure(frame, i, weight=1)
            Grid.columnconfigure(frame, i, weight=1)

        Button(game_win, text="Dismiss", command=game_win.destroy).grid(row=1,column=0)


    def __play(self,r,c):
        self.__game.play(r+1,c+1)
        for row,col in product(range(3), range(3)):
            self.__buttons[row][col].set(self.__game.at(row+1,col+1))

    def __quit(self):
        self.__root.quit()

    def run(self):
        self.__root.mainloop()

class Terminal(Ui):
    def __init__(self):
        self.__game = Game()

    def __get_input(self):
        while True:
            try: # Type check
                row = int(input("Enter row: "))
                col = int(input("Enter column:" ))
                if 1 <= row <= 3 and 1 <= col <= 3:
                    # Range check on input
                    break
                else:
                    print("Invalid input, please try again")
            except ValueError:
                print("Invalid input, please try again")
        return row,col

    def run(self):
        while self.__game.winner == None:
            print(self.__game)
            row,col = self.__get_input()
            try:
                self.__game.play(row,col)
            except GameError as e:
                print(e)

        print(self.__game)
        if self.__game.winner == Game.DRAW:
            print("The game was drawn")
        else:
            print(f"The winner is {self.__game.winner}")

