#script written for copilot to convert gif files to mp4

import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
import tkinter.scrolledtext as scrolledtext
from traceback import print_tb



class selfdow(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title('Gif converter')
        self.resizable(0,0)
        self.geometry('%dx%d+%d+%d' % (300, 300, 300, 10))
        self.main()

    def main(self):
        'Main instance method to create selfdow'
        Frame = ttk.LabelFrame(self, text='Converter')
        Frame.pack(expand=1, fill='both')

        # creating the entry boxes
        self.txt1 = tk.Label(Frame, text='Select Files:')
        self.txt1.place(relx=0.01, rely=0.05)

        # Add a Button Widget
        self.btn1 = ttk.Button(self, text="Select", command=self.open_file)
        self.btn1.place(relx=0.37, rely=0.09)

        #add a scrolled text field to show files choosen
        self.file_view = scrolledtext.ScrolledText(self, wrap='word', width=46, height=10, fg='gray')
        self.file_view['font'] = ('consolas', '12')
        self.file_view.place(relx=0.01, rely=0.22)

        # Add a Button Widget
        ttk.Button(self, text="Convert Files", command=self.convert_files).pack()

    def open_file(self):
        file = fd.askopenfilenames(parent=self, title='Choose a File')
        files_opened = self.splitlist(file)
        self.file_view.configure(state='normal')
        self.file_view.delete('1.0',tk.END)
        for elem in files_opened:
            filename = elem.split('/')[-1]
            self.file_view.insert(tk.INSERT, f'{filename}\n')
        self.file_view.configure(state ='disabled')
        
    def convert_files(self):
        pass


selfdow().mainloop()
