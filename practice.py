import tkinter as tk
import main as mainwin

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
BG_COLOR = "black"
TXT_COLOR1 = "white"
FONT = "Helvetica"
LBL_SIZE = 20
COLUMNS = 5

class Screen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg = BG_COLOR)
        self.gui_init()

    def gui_init(self):
        self.btn1 = tk.Button(self,
                                text = "Options",
                                font = (FONT, int(LBL_SIZE*1.25)),
                                bd = 0,
                                bg = BG_COLOR,
                                fg = TXT_COLOR1,
                                activebackground = TXT_COLOR1,
                                activeforeground = BG_COLOR)
        self.btn1.grid(row = 0, column = 2)
        self.lbl1 = tk.Label(self,
                                text = """Welcome to practice mode
Try to play the chord shown on the screen
Press Next to get a new chord""",
                                font = (FONT, LBL_SIZE),
                                bg = BG_COLOR,
                                fg = TXT_COLOR1)
        self.lbl1.grid(row = 1, column = 0, columnspan = COLUMNS)
