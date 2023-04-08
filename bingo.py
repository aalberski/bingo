# Adam Alberski
# 4/8/2023
# This is a simple program to simulate a bingo game by generating bingo boards with arrays and then randomly selecting numbers to be called out.

import random
import tkinter as tk

class bingo:
    # This dictionary is used to map the letters to the columns of the board.
    bingo_dict = dict({'B':0, 'I':1, 'N':2, 'G':3, 'O':4})

    # This function initializes the bingo board as a 5x5 matrix of zeros.
    def __init__(self, playername):
        self.playername = playername
        self.board = [[0 for x in range(5)] for y in range(5)]
        self.generateBoard()

    # This function generates a random number for the bingo board based on the letter passed to it from 'BINGO'.
    def generateNumber(self, letter):
        if letter == "B":
            return random.randint(1,15)
        elif letter == "I":
            return random.randint(16,30)
        elif letter == "N":
            return random.randint(31,45)
        elif letter == "G":
            return random.randint(46,60)
        elif letter == "O":
            return random.randint(61,75)
        else:
            return 0

    # This function fills the 5x5 matrix board with randomly generated numbers based on the letter associated with the current column.
    def generateBoard(self):
        for i in range(5):
            for j in range(5):
                self.board[i][j] = self.generateNumber(list(self.bingo_dict.keys())[j])
        self.board[2][2] = 'X'

    # This function returns a randomly called letter and number to be played.
    def callNumber(self):
        letter = random.choice('BINGO')
        number = self.generateNumber(letter)
        return letter, number
    
    # This function checks the board to see if the number called is on the board and if it is, it replaces it with an 'X'.
    def checkBoard(self, letter, number):
        for i in range(5):
            if self.board[i][self.bingo_dict[letter]] == number:
                self.board[i][self.bingo_dict[letter]] = 'X'
                return True
    
    # This function checks the board to see if there is a horizontal win.
    def horizontalWin(self):
        for i in range(5):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.board[i][3] == self.board[i][4] == 'X':
                return True
        return False
    
    # This function checks the board to see if there is a vertical win.
    def verticalWin(self):
        for i in range(5):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == self.board[3][i] == self.board[4][i] == 'X':
                return True
        return False
    
    # This function checks the board to see if there is a diagonal win.
    def diagonalWin(self):
        for i in range(5):
            if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.board[3][3] == self.board[4][4] == 'X':
                return True
            elif self.board[0][4] == self.board[1][3] == self.board[2][2] == self.board[3][1] == self.board[4][0] == 'X':
                return True
        return False
    
    # This function checks the board to see if there is a four corners win.
    def fourCorners(self):
        if self.board[0][0] == self.board[0][4] == self.board[4][0] == self.board[4][4] == 'X':
            return True
        return False
    
    # This function checks the board to see if there is a win.
    def checkWin(self):
        if self.horizontalWin() or self.verticalWin() or self.diagonalWin() or self.fourCorners():
            return True
        return False

    # This function displays the board.
    def display(self):
        s = "B\tI\tN\tG\tO"
        for i in range(5):
            s += "\n\n"
            for j in range(5):
                s += self.board[i][j].__str__() + "\t"
        return '\n' + s

# This is a GUI to give a visual to the bingo game
class bingoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Bingo")

    # This function is  a button that calls a new number.
    def callNumber(self, bingo):
        letter, number = bingo.callNumber()
        print("The number called is: " + letter + str(number))
        return letter, number

    # This function is called by the user to see if they won bingo.
    def callBingo(self, bingo):
        if bingo.checkWin():
            print("BINGO!")
            return True
        else:
            print("No bingo.")
            return False

def main():
    root = tk.Tk()
    root.geometry("400x300")
    app = bingoGUI(root)

    # Introduction to the game.
    title = tk.Label(root, text="Welcome to Bingo! \nEnter your name: ")
    playername = tk.Entry(root)
    game = bingo(playername.get())
    board = tk.Label(root, text=game.display())
    start = tk.Button(root, text="Start Game", command =lambda: [title.config(text = playername.get() + "'s Board: "), playername.destroy(), start.destroy(), board.pack(), callNum.pack(), callBingo.pack()])
    last = tk.Label(root, text="The number called is: ")
    title.pack()
    playername.pack()
    start.pack()

    # Buttons to call a number and to call bingo.
    callNum = tk.Button(root, text="Call Number", command = lambda: numCalled())
    def numCalled():
        letter,num = app.callNumber(game)
        last.config(text="The number called is: " + letter + str(num))
        last.pack()
        game.checkBoard(letter, num)
        board.config(text=game.display())

    callBingo = tk.Button(root, text="Bingo!", command = lambda: bingoCalled())
    def bingoCalled():
        if(app.callBingo(game)):
            callNum.destroy()
            callBingo.destroy()
            last.destroy()
            win = tk.Label(root, text="BINGO!")
            if(game.horizontalWin()):
                win.config(text="BINGO! \nHorizontal Win")
            elif(game.verticalWin()):
                win.config(text="BINGO! \nVertical Win")
            elif(game.diagonalWin()):
                win.config(text="BINGO! \nDiagonal Win")
            elif(game.fourCorners()):
                win.config(text="BINGO! \nFour Corners Win")
            win.pack()
            end = tk.Button(root, text="Exit", command = root.destroy)
            end.pack()
    root.mainloop()

if __name__ == "__main__":
    main()