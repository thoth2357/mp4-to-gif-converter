#script written for copilot to convert gif files to mp4

import tkinter as tk


class Window(tk.Tk):
    def __init__(self, screenName: str | None = ..., baseName: str | None = ..., className: str = ..., useTk: bool = ..., sync: bool = ..., use: str | None = ...) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title('Gif converter')
        self.resizable(0,0)
        