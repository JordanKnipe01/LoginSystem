import tkinter as tk
from database.CSC100DB import CSC100DB
from PIL import Image,ImageTk
from pdf2image import convert_from_path


db = CSC100DB()


class ReportPage(tk.Frame):

    def __init__(self, parent, controller):
        # self = this frame specific.
        tk.Frame.__init__(self, parent)
        # set controller to MainApp()
        self.controller = controller

        """report_frame = tk.Frame(self, width=480, height=240)
        report_frame.pack()"""

        # Generates monthly report
