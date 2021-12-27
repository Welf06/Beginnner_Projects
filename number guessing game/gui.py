import tkinter as tk
from tkinter import font


def start():
    # initialising the window
    window = tk.Tk()

    # defining the specification of the windows
    window.geometry("800x600")
    window.config(bg='#165050')
    window.resizable(width=False, height=False)
    window.title('Number Guessing Game')

    # defining labels
    title = tk.Label(window, text="Number Guessing Game",
                     font=('Ariel', 50), fg='white', bg='#165050')
    title.place(x=30, y=50)
    # defining buttons
    exit_button = tk.Button(window, text="EXIT", font=(
        'Arial', 30), fg='white', bg='Red', command=exit)
    exit_button.place(x=610, y=480)

    leaderboard_button = tk.Button(
        window, text="LEADERBOARD", font=('Arial', 30), fg='white', bg='Blue')
    leaderboard_button.place(x=240, y=480)

    play_button = tk.Button(window, text="PLAY", font=(
        'Arial', 30), fg='white', bg='Green')
    play_button.place(x=70, y=480)

    window.mainloop()


if __name__ == '__main__':
    start()
