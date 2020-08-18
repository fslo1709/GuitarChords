import tkinter as tk
import practice as win1
import timed_practice as win2
import memory_game as win3
import memorize as win4

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
BG_COLOR = "black"
TXT_COLOR1 = "white"
FONT = "Helvetica"
LBL_SIZE = 20

class mainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.title("Guitar Chords")
        self.configure(background = BG_COLOR)
        self.tScreen = Screen(self)
        self.tScreen.pack()

class Screen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg = BG_COLOR)
        self.root = parent
        self.gui_init()
        
    def gui_init(self):
        self.lbl1 = tk.Label(self,
                                text = """You can use this program to practice your guitar chords\n
Select one of the options to continue

""",
                                font = (FONT, LBL_SIZE),
                                bg = BG_COLOR,
                                fg = TXT_COLOR1)
        self.lbl1.grid(row = 0, column = 0)
        self.button1 = tk.Button(self,
                                 text = "Practice",
                                 font = (FONT, int(LBL_SIZE*1.25)),
                                 bd = 0,
                                 bg = BG_COLOR,
                                 fg = TXT_COLOR1,
                                 activebackground = TXT_COLOR1,
                                 activeforeground = BG_COLOR,
                                 command = self.open_frame1)
        self.button1.grid(row = 1, column = 0)
        self.button2 = tk.Button(self,
                                 text = "Timed Practice",
                                 font = (FONT, int(LBL_SIZE*1.25)),
                                 bd = 0,
                                 bg = BG_COLOR,
                                 fg = TXT_COLOR1,
                                 activebackground = TXT_COLOR1,
                                 activeforeground = BG_COLOR,
                                 command = self.open_frame2)
        self.button2.grid(row = 2, column = 0)

    def open_frame1(self):
        self.practiceWdw = tk.Toplevel(self.root)
        self.practiceWdw.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.practiceWdw.title("Practice Mode")
        self.practiceWdw.configure(background = win1.BG_COLOR)
        self.app1 = win1.Screen(self.practiceWdw)
        self.app1.pack()

    def open_frame2(self):
        self.timedPracticeWdw = tk.Toplevel(self.root)
        self.timedPracticeWdw.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.timedPracticeWdw.title("Timed Practice Mode")
        self.timedPracticeWdw.configure(background = win2.BG_COLOR)
        self.app2 = win2.Screen(self.timedPracticeWdw)
        self.app2.pack()
            
def main():
    app = mainApp()
    app.mainloop()

if __name__ == "__main__":
    main()
    print("Hello")
