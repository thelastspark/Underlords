import tkinter.font as font
from threading import Event, Thread
from tkinter import Frame, Tk, Label, BOTH, W, N, E, S, Entry, Toplevel, messagebox, CENTER, Message, Button
import tkinter
import main

# from tkinter.ttk import Frame
# import tkinter as tk
import configparser
import os
import re

from PIL import Image, ImageTk


class controlWindow(Frame):

    def __init__(self):
        super().__init__()
        # Where xray saves pictures
        self.workDir = None
        # Where the program will save fails
        self.saveDir = None
        # Where are model params
        self.modelDir = None
        self.dateCodeTx = None
        self.batchNumTx = None
        self.assemblyLineTx = None
        self.saveEnable = True
        self.numOfSpring = 42
        self.inspectWindow = None
        #        self.initUI()
        #        self.initConfig()
        self.update()


class ShopThread(Thread):
    def __init__(self, event, rootWindow, model):
        Thread.__init__(self)
        self.stopped = event
        self.model = model

        shopImages, classes, value, inspect, statesList = main.labelShop(model=model)

        self.shopLabels = []
        self.shopImages = []
        for i in range(5):
            shopFrame = Frame(
                master=rootWindow,
                relief=tkinter.RAISED,
                borderwidth=1
            )
            shopFrame.grid(row=0, column=i, padx=5, pady=5)

            tempImage = ImageTk.PhotoImage(shopImages[0])
            print(f"Confidence {statesList[i]*100}")
            label =label = Label(master=shopFrame, foreground='white', background='black', image=tempImage,
                          text=f"{classes[statesList[i]]} {value[i]*100:.1f}%", compound='top')
            self.shopLabels.append(label)
            label.pack()

    def run(self):
        while not self.stopped.wait(1):
            print("Updating store")
            shopImages, classes, value, inspect, statesList = main.labelShop(self.model)

            for i in range(5):
                tempImage = ImageTk.PhotoImage(shopImages[i])
                self.shopImages.append(tempImage)
                self.shopLabels[i].config(image=tempImage,
                          text=f"{classes[statesList[i]]} {value[i]*100:2.1f}%")


def openVision():
    root = Tk()
    # root.geometry("600x105")
    app = controlWindow()
    root.resizable(0, 0)

    model = main.createModel()

    stopFlag = Event()
    thread = ShopThread(stopFlag, root, model)
    thread.start()
    # this will stop the timer
    # stopFlag.set()

    # shopFrame.pack()

    root.mainloop()


def useles():
    print()
    # button = Button(
    #     text="Click me!",
    #     width=25,
    #     height=5,
    #     bg="blue",
    #     fg="yellow",
    # )
    # button.pack()
    # label = Label(
    #     master= shopFrame,
    #     text="This is the Shop!",
    #     fg="white",
    #     bg="black",
    #     width=10,
    #     height=10
    # )
    # label.pack()


openVision()
