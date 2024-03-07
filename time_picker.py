import ttkbootstrap as ttk

class TimePicker(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.hour = ttk.Spinbox(self, from_=0, to=23, width=2, format="%02.0f")
        self.minute = ttk.Spinbox(self, from_=0, to=59, width=2, format="%02.0f")
        self.hour.pack(side="left")
        self.minute.pack(side="left")

    def get_time(self):
        return (self.hour.get() or '0') + ':' + (self.minute.get() or '0')

    def set_time(self, values):
        self.hour.insert(0, values[0])
        self.minute.insert(0, values[1])
