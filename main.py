#script written for copilot to convert gif files to mp4

import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title('Gif converter')
        self.resizable(0,0)
        self.geometry('%dx%d+%d+%d' % (500, 300, 300, 10))
        self.main()

    def main(self):
        'Main instance method to create window'
        Frame = ttk.LabelFrame(self, text='Converter')
        Frame.pack(expand=1, fill='both')
        
Window().mainloop()
