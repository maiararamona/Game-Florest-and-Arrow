#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import Menubutton
from  code.menu import Menu
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(868, 603 ))

    def run(self):
        #pygame.mixer_music.load('./asset/somMenu.wav')
        #pygame.mixer_music.play(-1)
        #while True:
        menu = Menu(self.window)

        while True:
            menu.run()
            pass
