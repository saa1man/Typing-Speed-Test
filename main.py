from tkinter import *
from tkinter import messagebox
from words import word_list
from random import choice
from timeit import default_timer as timer

TITLE_FONT = ("Arial", 54, 'bold')
TITLE = "#00ADB5"
WORD_FONT = ("Times New Roman", 44)
ENTRY_FONT = ("Times New Roman", 24)
WORD = "#EEEEEE"
BACKGROUND = "#222831"
RANDOM_WORD = choice(word_list)
WORDS_TYPED = 0

def change_word():
    """New random word from word_list"""
    global RANDOM_WORD
    RANDOM_WORD = choice(word_list)
    typing_entry.delete(0, END)
    word_label.config(text=f"{RANDOM_WORD}")

def callback(sv):
    """Verify if you typed the right word + calculate final result"""
    global RANDOM_WORD, WORDS_TYPED
    current_letter = (len(sv.get()) - 1)
    start = timer()
    if start >= 30:
        # To calculate WPM: Count all typed entries and divide by five to get the number of words typed.
        messagebox.showinfo("Results", f"The results are: {(WORDS_TYPED / 5) / 0.5} WPM.")
    if sv.get() == RANDOM_WORD:
        WORDS_TYPED += len(RANDOM_WORD)
        change_word()
    elif sv.get():
        try:
            if sv.get()[current_letter] != RANDOM_WORD[current_letter]:
                word_label.config(text=f"{RANDOM_WORD}", bg="Red")
            else:
                word_label.config(text=f"{RANDOM_WORD}", bg=BACKGROUND)
        except IndexError:
            word_label.config(text=f"{RANDOM_WORD}", bg="Red")

# Creating App Window
screen = Tk()
screen.title("Typing test")
screen.config(padx=25, pady=25, bg=BACKGROUND)
screen.geometry("750x500")

# # Labels
title_label = Label(text='Typing Test', font=TITLE_FONT, fg=TITLE, bg=BACKGROUND)
title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

word_label = Label(text=RANDOM_WORD, font=WORD_FONT, fg=WORD, background=BACKGROUND)
word_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# # Check and trace typing 
sv=StringVar()
sv.trace('w', lambda name, index, mode, sv=sv:callback(sv))

# # Typing Entry
typing_entry = Entry(screen,width=15, font=ENTRY_FONT, textvariable=sv)
typing_entry.place(relx=0.5, rely=0.7, anchor=CENTER)
typing_entry.focus()


screen.mainloop()