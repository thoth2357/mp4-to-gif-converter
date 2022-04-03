#script written for copilot to convert gif files to mp4

import queue
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
import tkinter.scrolledtext as scrolledtext
import moviepy.editor as mp
from pathlib import Path
import os
from time import sleep
from timeit import timeit



class window(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title('Gif converter')
        self.resizable(0,0)
        self.geometry('%dx%d+%d+%d' % (300, 300, 300, 10))
        self.main()
        self.Time_to_run()

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
        
        # add progress bar
        self.tips = tk.Label(Frame, text='Status!!')
        self.tips.place(relx = 0.45, rely=0.75)
        self.progress_Bar = ttk.Progressbar(Frame, orient='horizontal', length=294, mode='indeterminate')
        self.progress_Bar.place(relx=0.00, rely=0.85)
        

        
        # Add a Button Widget
        ttk.Button(self, text="Convert Files", command=self.convert_files).pack()

    def open_file(self):
        file = fd.askopenfilenames(parent=self, title='Choose a File')
        self.files_opened = self.splitlist(file)
        self.file_view.configure(state='normal')
        self.file_view.delete('1.0',tk.END)
        for elem in self.files_opened:
            filename = elem.split('/')[-1]
            self.file_view.insert(tk.INSERT, f'{filename}\n')
        self.file_view.configure(state ='disabled')
        
    def convert_files(self):
        self.progress_bar()
        store_path = os.path.join(Path.home(), 'Documents/gif-to-mp4')
        if not os.path.isdir(store_path):
            os.makedirs(store_path)
        for file in self.files_opened:
            gif_clip = mp.VideoFileClip(file)
            gif_clip.write_videofile(f"{store_path}/{file.split('/')[-1]}.mp4")
        self.tips.configure(text='Completed')
        
    def progress_bar(self):
        self.progress_Bar['maximum'] = 100
        for i in range(100):
            self.tips.configure(text='Working on file')

            sleep(self.duration/100)
            self.progress_Bar['value'] = i
            self.progress_Bar.update()
            self.progress_Bar['value'] = 0
    
    def Time_to_run(self):
        Code_to_test = """def convert_files(self):
            store_path = os.path.join(Path.home(), 'Documents/gif-to-mp4')
            if not os.path.isdir(store_path):
                os.makedirs(store_path)
            for file in self.files_opened:
                gif_clip = mp.VideoFileClip(file)
                gif_clip.write_videofile(f"{store_path}/{file.split('/')[-1]}.mp4")
        """
        self.duration = timeit(Code_to_test)
        print('time', self.duration)
window().mainloop()
