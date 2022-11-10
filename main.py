# GUI TicTacToe using tkinter
import tkinter as tk
from tkinter import messagebox
import random


# Global variables
PLAYER = 'X'
COMPUTER = 'O'
TURN = 0

# Create a window
window = tk.Tk()
window.title('TicTacToe')
window.geometry('400x400')

# Create a frame
frame = tk.Frame(window)
frame.pack()

# Create a label
label = tk.Label(frame, text='TicTacToe', font=('Arial', 20))
label.pack()

# Create a canvas
canvas = tk.Canvas(frame, width=300, height=300)
canvas.pack()

# Create a button
button = tk.Button(frame, text='Reset', command=lambda: reset())
button.pack()

# Create a list of buttons
buttons = []
for i in range(3):
    buttons.append([])
    for j in range(3):
        buttons[i].append(tk.Button(canvas, text='', font=('Arial', 20), command=lambda i=i, j=j: click(i, j)))
        buttons[i][j].place(x=100 * i, y=100 * j, width=100, height=100)

# Create a function to reset the game
def reset():
    global TURN
    TURN = 0
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ''
            buttons[i][j]['state'] = 'normal'

# Create a function to check if there is a winner
def check():
    global TURN
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            if buttons[i][0]['text'] == PLAYER:
                messagebox.showinfo('Winner', 'You won!')
            else:
                messagebox.showinfo('Winner', 'You lost!')
            reset()
            return
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            if buttons[0][i]['text'] == PLAYER:
                messagebox.showinfo('Winner', 'You won!')
            else:
                messagebox.showinfo('Winner', 'You lost!')
            reset()
            return
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        if buttons[0][0]['text'] == PLAYER:
            messagebox.showinfo('Winner', 'You won!')
        else:
            messagebox.showinfo('Winner', 'You lost!')
        reset()
        return
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        if buttons[0][2]['text'] == PLAYER:
            messagebox.showinfo('Winner', 'You won!')
        else:
            messagebox.showinfo('Winner', 'You lost!')
        reset()
        return
    if TURN == 9:
        messagebox.showinfo('Winner', 'Draw!')
        reset()
        return

# Create a function to click on a button
def click(i, j):
    global TURN
    if buttons[i][j]['text'] == '':
        buttons[i][j]['text'] = PLAYER
        buttons[i][j]['state'] = 'disabled'
        TURN += 1
        check()
        COMPUTER_TURN()

# Create a function for the COMPUTER to make a move
def COMPUTER_TURN():
    global TURN
    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if buttons[i][j]['text'] == '':
            buttons[i][j]['text'] = COMPUTER
            buttons[i][j]['state'] = 'disabled'
            TURN += 1
            check()
            return

# Run the main loop
window.mainloop()
