import tkinter as tk
import practice
import timed_practice
import memory_game
import memorize

class mainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

class titleScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

if __name__ == "__main__":
