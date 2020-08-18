import tkinter as tk
import main as mainwin

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
BG_COLOR = "black"
TXT_COLOR1 = "white"
FONT = "Helvetica"
LBL_SIZE = 20

class Screen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg = BG_COLOR)
        self.gui_init()

    def gui_init(self):
        self.lbl1 = tk.Label(self,
                                text = """Welcome to timed practice mode
Try to play the chord shown on the screen within the time limit
You can change the time limit using the slider on the right side
Press Next to get a new chord
When you're ready, press Start""",
                                font = (FONT, LBL_SIZE),
                                bg = BG_COLOR,
                                fg = TXT_COLOR1)
        self.lbl1.pack()
