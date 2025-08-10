from tkinter import *
from game import show_chess_board
import pygame


pygame.mixer.init()
click_sound_start = pygame.mixer.Sound("button_click_sound.wav")

def start_game():
    click_sound_start.play()
    start_screen.withdraw()
    show_chess_board(start_screen)


start_screen = Tk()
start_screen.geometry('800x800')
start_screen.title('Welcome to Chess')
background = PhotoImage(file='chess_pic.png')
background_label = Label(start_screen, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

background_btn = PhotoImage(file='start_game.png',).subsample(1, 1)


start_button = Button(start_screen, image=background_btn, command=start_game)
start_button.place(relx=0.55,rely=0.4)

start_screen.mainloop()
