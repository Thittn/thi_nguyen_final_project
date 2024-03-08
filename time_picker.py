# File: time_picker.py
# Author: Thi Nguyen
# Date: 03/08/2024
# Description: This file contains the implementation of the TimePicker class,
#              which provides a widget for selecting time (hour and minute) using Spinboxes


import ttkbootstrap as ttk

class TimePicker(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        # Create Spinboxes for hour and minute selection
        self.hour = ttk.Spinbox(self, from_=0, to=23, width=2, format="%02.0f")
        self.minute = ttk.Spinbox(self, from_=0, to=59, width=2, format="%02.0f")
        # Pack Spinboxes to the left side
        self.hour.pack(side="left")
        self.minute.pack(side="left")

    #Get the selected time
    def get_time(self):
        # Concatenate hour and minute values and return as string
        return (self.hour.get() or '') + ':' + (self.minute.get() or '')

    #Set the time in the TimePicker
    def set_time(self, values):
        # Set hour and minute values from the given list
        self.hour.insert(0, values[0])
        self.minute.insert(0, values[1])
