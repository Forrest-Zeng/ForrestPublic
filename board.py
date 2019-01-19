#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created on Tue Nov 27 20:33:13 2018

author: Forrest Zeng
"""

import queue
from tkinter import *
import threading
from random import choice, randint
import time
import AIData as ai

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800

# Chessboard diameter
D = 40
# start point
BLACK_START = (380, 7)
RED_START = (390, 800 - 60)

# Row interval step pixels
ROW_STEP = 27
# Col interval step pixels
COL_STEP = 47

q = queue.Queue(maxsize=1)

q2 = queue.Queue(maxsize=1)

#ttq = queue.Queue()

startChoice = ["True", "False"]
rPlayed = choice(startChoice)

class UI():
    def __init__(self): 
#        move = q.get()
#        mMove = tq.get()
        self.root = Tk()
        self.startChoice = ["True","False"]
        rPlayed = choice(self.startChoice)
        self.BLACK_LIST = []
        self.RED_LIST = []
        self.RED_TEXT = []
        self.RED_NUM = 10
        self.RED_POS = [121,115,114,113,112,118,117,116,119,120]
        self.BLACK_POS = [1,7,8,9,10,4,5,6,2,3]
#        self.ALL_COORD = "{}-{}".format(self.RED_POS, self.BLACK_POS)
        self.AIDO = ai.AIDO
        self.AINDO = ai.AINDO
        self.canvas = Canvas(self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)  # Make a little board i can draw o
        self.gameOn = True
        self.ALL = "{}-{}".format(self.RED_POS, self.BLACK_POS)
        self.index = -1
#        self.CUR_MOVE = "{}-{}".format(move, mMove)
#        self.ALL = {self.ALL_COORD:self.CUR_MOVE}
    def draw_oval(self, color, x0, y0): 
        return "{}-{}".format(color, self.canvas.create_oval(x0, y0, x0 + D, y0 + D, fill=color))
    
    def draw_text(self, TEXT0, x0, y0  ): 
        return "{}-{}".format(TEXT0, self.canvas.create_text(x0 , y0 , text = str(TEXT0)))

    def get_ready(self): 
        # black init
        for i in range(4):
            for j in range(i + 1):
                self.BLACK_LIST.append(
                    self.draw_oval("black", BLACK_START[0] - (i - 2 * j) * ROW_STEP, BLACK_START[1] + i * COL_STEP))

        # red init
        for i in range(4):
            for j in range(i + 1):
                self.RED_LIST.append(
                    self.draw_oval("red", RED_START[0] - (i - 2 * j) * ROW_STEP, RED_START[1] - i * COL_STEP))
        for i in range(4):
            for j in range(i + 1):
                
                self.RED_NUM-=1
                self.RED_NUM0 = self.RED_NUM + 1
                if self.RED_NUM0 == 10:
                    self.RED_NUM0 = 0
#                self.PRESERVE = self.RED_NUM
                if self.RED_NUM == 9:
                    self.RED_NUM == -1
#                self.RED_TEXT = []
#                self.RED_TEXT.append()
                self.RED_TEXT.append(
                    self.draw_text(self.RED_NUM0,  RED_START[0] - (i - 2 * j) * ROW_STEP, RED_START[1] - i * COL_STEP))
                if self.RED_NUM0 == 0:
                    self.RED_NUM0 = self.RED_NUM + 1
    def redMove(self, checker, direction): 
        self.checker = int(checker)
#        point = self.RED_LIST[checker]
        direction = int(direction)
        self.rChm = -ROW_STEP 
        self.rChmc = -COL_STEP
        if direction == 1:
            self.rChm =  -COL_STEP
            self.rChmc = -ROW_STEP 
            if self.RED_POS[self.checker] == 121:
                cur_move = self.RED_POS[self.checker] - 2
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 121 & self.RED_POS[self.checker] > 118:
                cur_move = self.RED_POS[self.checker] - 3
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 119 & self.RED_POS[self.checker] > 115:
                cur_move = self.RED_POS[self.checker] - 4
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 116 & self.RED_POS[self.checker] < 110 :
                cur_move = self.RED_POS[self.checker] - 9
                self.RED_POS[self.checker] = self.RED_POS[self.checker] - 9
            if self.RED_POS[self.checker] < 112 & self.RED_POS[self.checker] > 96:
                cur_move = self.RED_POS[self.checker] - 15
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 97 & self.RED_POS[self.checker] < 83:
                cur_move = self.RED_POS[self.checker] - 13
            if self.RED_POS[self.checker] < 84 + 2 & self.RED_POS[self.checker] > 71 + 2:
                cur_move = self.RED_POS[self.checker] - 12
            if self.RED_POS[self.checker] < 72 + 2& self.RED_POS[self.checker] > 61 + 2:
                cur_move = self.RED_POS[self.checker] - 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 62 + 2& self.RED_POS[self.checker] > 52 + 2:
                cur_move = self.RED_POS[self.checker] - 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 61 + 2& self.RED_POS[self.checker] < 51 + 2:
                cur_move = self.RED_POS[self.checker] - 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 53 + 2 & self.RED_POS[self.checker] >42 +2:
                cur_move = self.RED_POS[self.checker] - 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 43 + 2& self.RED_POS[self.checker] > 33 + 2:
                cur_move = self.RED_POS[self.checker] - 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 34 & self.RED_POS[self.checker] > 23:
                cur_move = self.RED_POS[self.checker] - 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 24 & self.RED_POS[self.checker] > 10:
                cur_move = self.RED_POS[self.checker] - 7
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 11 & self.RED_POS[self.checker] > 6:
                cur_move = self.RED_POS[self.checker] - 4
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 7 & self.RED_POS[self.checker] > 3:
                cur_move = self.RED_POS[self.checker] - 3
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 4 & self.RED_POS[self.checker] > 1:
                cur_move = self.RED_POS[self.checker] - 2
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] == 1:
                cur_move = self.RED_POS[self.checker] - 1
                self.RED_POS[self.checker] = cur_move
            print(self.RED_POS[self.checker])
        if direction == 2:
            self.rChm =  -COL_STEP 
            self.rChmc = ROW_STEP
            if self.RED_POS[self.checker] == 121:
                cur_move = self.RED_POS[self.checker] - 1
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 121 & self.RED_POS[self.checker] > 118:
                cur_move = self.RED_POS[self.checker] - 2
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 119 & self.RED_POS[self.checker] > 115:
                cur_move = self.RED_POS[self.checker] - 3
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 116 & self.RED_POS[self.checker] < 110 :
                cur_move = self.RED_POS[self.checker] - 8
                self.RED_POS[self.checker] = self.RED_POS[self.checker] - 9
            if self.RED_POS[self.checker] < 112 & self.RED_POS[self.checker] > 96:
                cur_move = self.RED_POS[self.checker] - 14
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 97 & self.RED_POS[self.checker] < 83:
                cur_move = self.RED_POS[self.checker] - 12
            if self.RED_POS[self.checker] < 84 + 2 & self.RED_POS[self.checker] > 71 + 2:
                cur_move = self.RED_POS[self.checker] - 11
            if self.RED_POS[self.checker] < 72 + 2& self.RED_POS[self.checker] > 61 + 2:
                cur_move = self.RED_POS[self.checker] - 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 62 + 2& self.RED_POS[self.checker] > 52 + 2:
                cur_move = self.RED_POS[self.checker] - 9
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 61 + 2& self.RED_POS[self.checker] < 51 + 2:
                cur_move = self.RED_POS[self.checker] - 9
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 53 + 2 & self.RED_POS[self.checker] >42 +2:
                cur_move = self.RED_POS[self.checker] - 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 43 + 2& self.RED_POS[self.checker] > 33 + 2:
                cur_move = self.RED_POS[self.checker] - 9
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 34 & self.RED_POS[self.checker] > 23:
                cur_move = self.RED_POS[self.checker] - 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 24 & self.RED_POS[self.checker] > 10:
                cur_move = self.RED_POS[self.checker] - 6
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 11 & self.RED_POS[self.checker] > 6:
                cur_move = self.RED_POS[self.checker] - 3
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 7 & self.RED_POS[self.checker] > 3:
                cur_move = self.RED_POS[self.checker] - 2
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 4 & self.RED_POS[self.checker] > 1:
                cur_move = self.RED_POS[self.checker] - 1
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] == 1:
                cur_move = self.RED_POS[self.checker] - 0
                self.RED_POS[self.checker] = cur_move
        if direction == 3:
            self.rChm = 0
            self.rChmc = COL_STEP
            cur_move = self.RED_POS[self.checker] - 1
            self.RED_POS[self.checker]  = cur_move
        if direction == 4:
            self.rChm = COL_STEP 
            self.rChmc = ROW_STEP
            if self.RED_POS[self.checker] == 121:
                cur_move = self.RED_POS[self.checker] + 1
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 121 & self.RED_POS[self.checker] > 118:
                cur_move = self.RED_POS[self.checker] + 2
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 119 & self.RED_POS[self.checker] > 115:
                cur_move = self.RED_POS[self.checker] + 3
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 116 & self.RED_POS[self.checker] < 110 :
                cur_move = self.RED_POS[self.checker] + 4
                self.RED_POS[self.checker] = self.RED_POS[self.checker] + 9
            if self.RED_POS[self.checker] < 112 & self.RED_POS[self.checker] > 96:
                cur_move = self.RED_POS[self.checker] + 8
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 97 & self.RED_POS[self.checker] < 83:
                cur_move = self.RED_POS[self.checker] + 15
            if self.RED_POS[self.checker] < 84 + 2 & self.RED_POS[self.checker] > 71 + 2:
                cur_move = self.RED_POS[self.checker] + 13
            if self.RED_POS[self.checker] < 72 + 2& self.RED_POS[self.checker] > 61 + 2:
                cur_move = self.RED_POS[self.checker] + 12
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 62 + 2& self.RED_POS[self.checker] > 52 + 2:
                cur_move = self.RED_POS[self.checker] + 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 61 + 2& self.RED_POS[self.checker] < 51 + 2:
                cur_move = self.RED_POS[self.checker] + 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 53 + 2 & self.RED_POS[self.checker] >42 +2:
                cur_move = self.RED_POS[self.checker] + 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 43 + 2& self.RED_POS[self.checker] > 33 + 2:
                cur_move = self.RED_POS[self.checker] + 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 34 & self.RED_POS[self.checker] > 23:
                cur_move = self.RED_POS[self.checker] + 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 24 & self.RED_POS[self.checker] > 10:
                cur_move = self.RED_POS[self.checker] + 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 11 & self.RED_POS[self.checker] > 6:
                cur_move = self.RED_POS[self.checker] + 7
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 7 & self.RED_POS[self.checker] > 3:
                cur_move = self.RED_POS[self.checker] + 4
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 4 & self.RED_POS[self.checker] > 1:
                cur_move = self.RED_POS[self.checker] + 3
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] == 1:
                cur_move = self.RED_POS[self.checker] + 2
                self.RED_POS[self.checker] = cur_move
        if direction == 5:
            self.rChm = COL_STEP
            self.rChmc = -ROW_STEP
            if self.RED_POS[self.checker] == 121:
                cur_move = self.RED_POS[self.checker] + 1
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 121 & self.RED_POS[self.checker] > 118:
                cur_move = self.RED_POS[self.checker] + 1
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 119 & self.RED_POS[self.checker] > 115:
                cur_move = self.RED_POS[self.checker] + 1
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 116 & self.RED_POS[self.checker] < 110 :
                cur_move = self.RED_POS[self.checker] + 1
                self.RED_POS[self.checker] = self.RED_POS[self.checker] + 9
            if self.RED_POS[self.checker] < 112 & self.RED_POS[self.checker] > 96:
                cur_move = self.RED_POS[self.checker] + 15
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 97 & self.RED_POS[self.checker] < 83:
                cur_move = self.RED_POS[self.checker] + 13
            if self.RED_POS[self.checker] < 84 + 2 & self.RED_POS[self.checker] > 71 + 2:
                cur_move = self.RED_POS[self.checker] + 12
            if self.RED_POS[self.checker] < 72 + 2& self.RED_POS[self.checker] > 61 + 2:
                cur_move = self.RED_POS[self.checker] + 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 62 + 2& self.RED_POS[self.checker] > 52 + 2:
                cur_move = self.RED_POS[self.checker] + 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 61 + 2& self.RED_POS[self.checker] < 51 + 2:
                cur_move = self.RED_POS[self.checker] + 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 53 + 2 & self.RED_POS[self.checker] >42 +2:
                cur_move = self.RED_POS[self.checker] + 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 43 + 2& self.RED_POS[self.checker] > 33 + 2:
                cur_move = self.RED_POS[self.checker] + 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 34 & self.RED_POS[self.checker] > 23:
                cur_move = self.RED_POS[self.checker] + 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 24 & self.RED_POS[self.checker] > 10:
                cur_move = self.RED_POS[self.checker] + 7
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 11 & self.RED_POS[self.checker] > 6:
                cur_move = self.RED_POS[self.checker] + 4
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 7 & self.RED_POS[self.checker] > 3:
                cur_move = self.RED_POS[self.checker] + 3
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 4 & self.RED_POS[self.checker] > 1:
                cur_move = self.RED_POS[self.checker] + 2
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] == 1:
                cur_move = self.RED_POS[self.checker] + 1
                self.RED_POS[self.checker] = cur_move
        if direction == 6:
            self.rChm = 0
            self.rChmc = -COL_STEP
            cur_move = self.RED_POS[self.checker] + 1
            self.RED_POS[self.checker] = cur_move
        self.canvas.move(self.RED_LIST[-checker].split("-")[1], self.rChmc, self.rChm)
        self.canvas.move(self.RED_TEXT[-checker].split("-")[1], self.rChmc, self.rChm) 
#        self.RED_LIST.insert(0, last)
    def blackMove(self,checker, direction): 
        self.checker = int(checker)
#        point = self.RED_LIST[checker]
        direction = int(direction)
        self.rChm = -ROW_STEP 
        self.rChmc = -COL_STEP
        if direction == 1:
            self.rChm =  -COL_STEP
            self.rChmc = -ROW_STEP 
            if self.RED_POS[self.checker] == 121:
                cur_move = self.RED_POS[self.checker] - 2
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 121 & self.RED_POS[self.checker] > 118:
                cur_move = self.RED_POS[self.checker] - 3
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 119 & self.RED_POS[self.checker] > 115:
                cur_move = self.RED_POS[self.checker] - 4
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 116 & self.RED_POS[self.checker] < 110 :
                cur_move = self.RED_POS[self.checker] - 9
                self.RED_POS[self.checker] = self.RED_POS[self.checker] - 9
            if self.RED_POS[self.checker] < 112 & self.RED_POS[self.checker] > 96:
                cur_move = self.RED_POS[self.checker] - 15
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 97 & self.RED_POS[self.checker] < 83:
                cur_move = self.RED_POS[self.checker] - 13
            if self.RED_POS[self.checker] < 84 + 2 & self.RED_POS[self.checker] > 71 + 2:
                cur_move = self.RED_POS[self.checker] - 12
            if self.RED_POS[self.checker] < 72 + 2& self.RED_POS[self.checker] > 61 + 2:
                cur_move = self.RED_POS[self.checker] - 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 62 + 2& self.RED_POS[self.checker] > 52 + 2:
                cur_move = self.RED_POS[self.checker] - 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 61 + 2& self.RED_POS[self.checker] < 51 + 2:
                cur_move = self.RED_POS[self.checker] - 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 53 + 2 & self.RED_POS[self.checker] >42 +2:
                cur_move = self.RED_POS[self.checker] - 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 43 + 2& self.RED_POS[self.checker] > 33 + 2:
                cur_move = self.RED_POS[self.checker] - 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 34 & self.RED_POS[self.checker] > 23:
                cur_move = self.RED_POS[self.checker] - 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 24 & self.RED_POS[self.checker] > 10:
                cur_move = self.RED_POS[self.checker] - 7
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 11 & self.RED_POS[self.checker] > 6:
                cur_move = self.RED_POS[self.checker] - 4
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 7 & self.RED_POS[self.checker] > 3:
                cur_move = self.RED_POS[self.checker] - 3
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 4 & self.RED_POS[self.checker] > 1:
                cur_move = self.RED_POS[self.checker] - 2
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] == 1:
                cur_move = self.RED_POS[self.checker] - 1
                self.RED_POS[self.checker] = cur_move
            print(self.RED_POS[self.checker])
        if direction == 2:
            self.rChm =  -COL_STEP 
            self.rChmc = ROW_STEP
            if self.RED_POS[self.checker] == 121:
                cur_move = self.RED_POS[self.checker] - 1
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 121 & self.RED_POS[self.checker] > 118:
                cur_move = self.RED_POS[self.checker] - 2
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 119 & self.RED_POS[self.checker] > 115:
                cur_move = self.RED_POS[self.checker] - 3
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 116 & self.RED_POS[self.checker] < 110 :
                cur_move = self.RED_POS[self.checker] - 8
                self.RED_POS[self.checker] = self.RED_POS[self.checker] - 9
            if self.RED_POS[self.checker] < 112 & self.RED_POS[self.checker] > 96:
                cur_move = self.RED_POS[self.checker] - 14
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 97 & self.RED_POS[self.checker] < 83:
                cur_move = self.RED_POS[self.checker] - 12
            if self.RED_POS[self.checker] < 84 + 2 & self.RED_POS[self.checker] > 71 + 2:
                cur_move = self.RED_POS[self.checker] - 11
            if self.RED_POS[self.checker] < 72 + 2& self.RED_POS[self.checker] > 61 + 2:
                cur_move = self.RED_POS[self.checker] - 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 62 + 2& self.RED_POS[self.checker] > 52 + 2:
                cur_move = self.RED_POS[self.checker] - 9
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 61 + 2& self.RED_POS[self.checker] < 51 + 2:
                cur_move = self.RED_POS[self.checker] - 9
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 53 + 2 & self.RED_POS[self.checker] >42 +2:
                cur_move = self.RED_POS[self.checker] - 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 43 + 2& self.RED_POS[self.checker] > 33 + 2:
                cur_move = self.RED_POS[self.checker] - 9
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 34 & self.RED_POS[self.checker] > 23:
                cur_move = self.RED_POS[self.checker] - 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 24 & self.RED_POS[self.checker] > 10:
                cur_move = self.RED_POS[self.checker] - 6
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 11 & self.RED_POS[self.checker] > 6:
                cur_move = self.RED_POS[self.checker] - 3
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 7 & self.RED_POS[self.checker] > 3:
                cur_move = self.RED_POS[self.checker] - 2
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 4 & self.RED_POS[self.checker] > 1:
                cur_move = self.RED_POS[self.checker] - 1
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] == 1:
                cur_move = self.RED_POS[self.checker] - 0
                self.RED_POS[self.checker] = cur_move
        if direction == 3:
            self.rChm = 0
            self.rChmc = COL_STEP
            cur_move = self.RED_POS[self.checker] - 1
            self.RED_POS[self.checker]  = cur_move
        if direction == 4:
            self.rChm = COL_STEP 
            self.rChmc = ROW_STEP
            if self.RED_POS[self.checker] == 121:
                cur_move = self.RED_POS[self.checker] + 1
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 121 & self.RED_POS[self.checker] > 118:
                cur_move = self.RED_POS[self.checker] + 2
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 119 & self.RED_POS[self.checker] > 115:
                cur_move = self.RED_POS[self.checker] + 3
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 116 & self.RED_POS[self.checker] < 110 :
                cur_move = self.RED_POS[self.checker] + 4
                self.RED_POS[self.checker] = self.RED_POS[self.checker] + 9
            if self.RED_POS[self.checker] < 112 & self.RED_POS[self.checker] > 96:
                cur_move = self.RED_POS[self.checker] + 8
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 97 & self.RED_POS[self.checker] < 83:
                cur_move = self.RED_POS[self.checker] + 15
            if self.RED_POS[self.checker] < 84 + 2 & self.RED_POS[self.checker] > 71 + 2:
                cur_move = self.RED_POS[self.checker] + 13
            if self.RED_POS[self.checker] < 72 + 2 & self.RED_POS[self.checker] > 61 + 2:
                cur_move = self.RED_POS[self.checker] + 12
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 62 + 2 & self.RED_POS[self.checker] > 52 + 2:
                cur_move = self.RED_POS[self.checker] + 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 61 + 2 & self.RED_POS[self.checker] < 51 + 2:
                cur_move = self.RED_POS[self.checker] + 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 53 + 2 & self.RED_POS[self.checker] >42 +2:
                cur_move = self.RED_POS[self.checker] + 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 43 + 2& self.RED_POS[self.checker] > 33 + 2:
                cur_move = self.RED_POS[self.checker] + 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 34 & self.RED_POS[self.checker] > 23:
                cur_move = self.RED_POS[self.checker] + 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 24 & self.RED_POS[self.checker] > 10:
                cur_move = self.RED_POS[self.checker] + 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 11 & self.RED_POS[self.checker] > 6:
                cur_move = self.RED_POS[self.checker] + 7
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 7 & self.RED_POS[self.checker] > 3:
                cur_move = self.RED_POS[self.checker] + 4
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 4 & self.RED_POS[self.checker] > 1:
                cur_move = self.RED_POS[self.checker] + 3
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] == 1:
                cur_move = self.RED_POS[self.checker] + 2
                self.RED_POS[self.checker] = cur_move
        if direction == 5:
            self.rChm = COL_STEP
            self.rChmc = -ROW_STEP
            if self.RED_POS[self.checker] == 121:
                cur_move = self.RED_POS[self.checker] + 1
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 121 & self.RED_POS[self.checker] > 118:
                cur_move = self.RED_POS[self.checker] + 1
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 119 & self.RED_POS[self.checker] > 115:
                cur_move = self.RED_POS[self.checker] + 1
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 116 & self.RED_POS[self.checker] < 110 :
                cur_move = self.RED_POS[self.checker] + 1
                self.RED_POS[self.checker] = self.RED_POS[self.checker] + 9
            if self.RED_POS[self.checker] < 112 & self.RED_POS[self.checker] > 96:
                cur_move = self.RED_POS[self.checker] + 15
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 97 & self.RED_POS[self.checker] < 83:
                cur_move = self.RED_POS[self.checker] + 13
            if self.RED_POS[self.checker] < 84 + 2 & self.RED_POS[self.checker] > 71 + 2:
                cur_move = self.RED_POS[self.checker] + 12
            if self.RED_POS[self.checker] < 72 + 2& self.RED_POS[self.checker] > 61 + 2:
                cur_move = self.RED_POS[self.checker] + 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 62 + 2& self.RED_POS[self.checker] > 52 + 2:
                cur_move = self.RED_POS[self.checker] + 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] > 61 + 2& self.RED_POS[self.checker] < 51 + 2:
                cur_move = self.RED_POS[self.checker] + 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 53 + 2 & self.RED_POS[self.checker] >42 +2:
                cur_move = self.RED_POS[self.checker] + 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 43 + 2& self.RED_POS[self.checker] > 33 + 2:
                cur_move = self.RED_POS[self.checker] + 10
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 34 & self.RED_POS[self.checker] > 23:
                cur_move = self.RED_POS[self.checker] + 11
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 24 & self.RED_POS[self.checker] > 10:
                cur_move = self.RED_POS[self.checker] + 7
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 11 & self.RED_POS[self.checker] > 6:
                cur_move = self.RED_POS[self.checker] + 4
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 7 & self.RED_POS[self.checker] > 3:
                cur_move = self.RED_POS[self.checker] + 3
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] < 4 & self.RED_POS[self.checker] > 1:
                cur_move = self.RED_POS[self.checker] + 2
                self.RED_POS[self.checker] = cur_move
            if self.RED_POS[self.checker] == 1:
                cur_move = self.RED_POS[self.checker] + 1
                self.RED_POS[self.checker] = cur_move
        if direction == 6:
            self.rChm = 0
            self.rChmc = -COL_STEP
        self.canvas.move(self.BLACK_LIST[-checker].split("-")[1], self.rChmc, self.rChm)

    def move_event(self):
        
        while self.gameOn:
            try:
                global rPlayed
                print("This is the DO list\n")
                print(self.AIDO)
                print("\nThis is the DON'T do list\n")
                print(self.AINDO)
                self.index+=1
                index0 = str(self.index)
                move = q.get()
                #ask = tq.get()
#                print("DEDBUG 1")
                
                if rPlayed == "False":
                    move = q.get()
#                    ttq.put(turn)
#                    q2.put("What do you move?:")
#                    move = q.get()
                    mMove = "null"
#                    mChecker0 = "null"
                    mTimes = int(move[0])
                    mChecker = int(move[2])
                    mDirection = int(move[4])
#                    mDirection0 = mDirection + 3
#                    if mDirection0 == 7: 
#                        mDirection0 = 1
#                    if mDirection0 == 8: 
#                        mDirection0 = 2
#                    if mDirection0 == 9: 
#                        mDirection0 = 3
#                    mMove = "{}-{}-{}".format(mTimes,mChecker,mDirection0)
#                    mAll = [self.ALL,mMove]
                    print("red will go.")
                    for t in range(mTimes):
                        self.redMove(mChecker, mDirection)
                    rPlayed = "True"
#                    ask = input("Was that a good move?:")
#                    if ask == "Y":
#                        self.AIDO.update({index0:mAll})
#                        rPlayed = "True"
#                    if ask == "N":
#                        self.AINDO.update({index0:mAll})
#                        rPlayed = "True"
#                    if ask == "E":
#                        self.AINDO.update({index0:mAll})
#                        rPlayed = "True"
                    #self.redMove(1,1)
#                    ttq.put("Black")
#                    for i in range(0,54):
#                        for j in range(0,9):
#                            for k in range(1,6):
#                                self.AINDO[i] = {self.ALL:"{}:{}:{}".format(0,j,k)}
                if rPlayed == "True":
                    while rPlayed == "True":
                        print(self.AIDO)
                        print(self.AINDO)
                        print("black will go.")
    #                    ttq.put("Black")
                        mMove = "null"
                        for i in range(0, len(self.AIDO)):
                            i0 = str(i)
                            if len(self.AIDO) > 5 & len(self.AINDO) > 5:
                                if self.AIDO[i0][0] == self.ALL:
                                    mMove = "{}:{}:{}".format(mTimes,mChecker,mDirection)
                                    mMove0 = self.AIDO[i0][1]
                                    mTimes = int(mMove0[0])
                                    mChecker = int(mMove0[2])
                                    mDirection = int(mMove0[4])
                                else:
                                    mTimes = int(randint(11,3))
                                    mChecker = int(randint(0,9))
                                    mDirection = int(randint(1,6))
                                    if self.AINDO[i0][1] == mMove:
                                        mTimes = int(randint(1,3))
                                        mChecker = int(randint(0,9))
                                        mDirection = int(randint(1,6))
                            else:
                                mTimes = int(randint(1,3))
                                mChecker = int(randint(0,9))
                                mDirection = int(randint(1,6))
                        mMove = "{}:{}:{}".format(mTimes,mChecker,mDirection)
                        mALL = {self.ALL:mMove}
                        for t in range(mTimes):     
                            self.blackMove(mChecker,mDirection)
#                        ask0 = input("Was that a good move?:")
                        q2.put("Was that a good move?:")
                        ask0 = q.get()
                        if ask0 == "Y": 
                            self.AIDO[index0] = mALL
                            rPlayed = "False"
                        if ask0 == "N": 
                            self.AINDO[index0] = mALL
                            rPlayed = "False"
                        if ask0 == "E":  
                            self.AINDO[index0] = mALL
                            for t in range(mTimes):     
                                mDirection0 = mDirection + 3
                                if mDirection > 3 & mDirection < 7:
                                    mDirection0 = mDirection - 3
#                                if mDirection0 == 8: 
#                                    mDirection0 = 2
#                                if mDirection0 == 9: 
#                                    mDirection0 = 3
                                self.blackMove(mChecker,mDirection0)
                            print("Ok, got it. Let me go again.")
                            rPlayed = "True"
                        if ask0 == "C":
                            self.AINDO[index0] = mALL
                            for t in range(mTimes):     
                                mDirection0 = mDirection + 3
                                if mDirection > 3 & mDirection < 7:
                                    mDirection0 = mDirection - 3
#                                if mDirection0 == 8: 
#                                    mDirection0 = 2
#                                if mDirection0 == 9: 
#                                    mDirection0 = 3
                                self.blackMove(mChecker,mDirection0)
                            rPlayed = "False"
#                            for i in range(0,54):
#                                for j in range(0,9):
#                                    for k in range(1,6):
#                                        self.AINDO[i] = {self.ALL:"{}:{}:{}".format(0,j,k)}
    #                ttq.put("Red")
                    # sleep 100ms
                    time.sleep(0.1)
            except queue.Empty: 
                pass

    def input_event(self): 
        while self.gameOn:
#            turn = ttq.get()
#            while turn == "Black":
#            if turn == "Red"
            move = "null"
#
            move = str(input("What do you move?:"))
#            #ask = str(input("Was that a good move?:"))
##            if rPlayed == "True":
##                ask = str(input("Was that a good move?:"))
#            #direction = input("What direction?")
#            #direction = int(direction)
            q.put(move)
#            tq.put(ask)
            next = None
            try:
                quest = q2.get(timeout=2)
                if quest:
                    next = input(quest)
                    q.put(next)
            except queue.Empty:
                pass
            #q.put(direction)
            if next == "over":
                self.gameOn = False
            

    def run(self): 
        board = PhotoImage(file="board.png")  # The board photo
        self.canvas.create_image(0, 0, anchor=NW, image=board)
        self.get_ready()
        self.canvas.pack()
        t1 = threading.Thread(target=self.input_event)
        t1.daemon = True
        t1.start()
        t2 = threading.Thread(target=self.move_event)
        t2.daemon = True
        t2.start()

        self.root.mainloop()
 

if __name__ == '__main__': 
    UI().run()
    #task = []
    #t1 = threading.Thread(name="ui", target=UI().run)
    #t1.daemon = True
    #t1.start()
    #t1.join()
