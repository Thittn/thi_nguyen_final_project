import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import DateEntry
import tkinter.font as tkFont
from base_page import BasePage
from time_picker import TimePicker
from constants import *

class PageTwo(BasePage):


    def render_title(self, container):
        self.img = ttk.PhotoImage(file='fill_form.png', width=179, height=141)
        ttk.Label(container, image=self.img).pack()

        #Add and format welcome text to top of the page
        bold = tkFont.Font(family='Times', size=30)
        ttk.Label(container, text='Make Your Booking Today', font=bold, justify=LEFT).pack()


    def render_body(self, container):
        left_container = ttk.Frame(container)
        left_container.grid(row=0, column=0, sticky=W)
        right_container = ttk.Frame(container)
        right_container.grid(row=0, column=1, sticky=W)
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)

        ttk.Label(left_container, text='Choose date and time').pack(anchor=W, padx=60, pady=(0, 10))
        date_time_container = ttk.Frame(left_container)
        date_time_container.pack(anchor=W, padx=50)
        date_time_container.grid_columnconfigure(0, pad=20)
        self.date_entry = DateEntry(date_time_container)
        self.date_entry.grid(row=0, column=0)
        self.time_entry = TimePicker(date_time_container)
        self.time_entry.grid(row=0, column=1)
        self.services_entry = []

        ttk.Label(left_container, text='Choose services').pack(anchor=W, padx=60, pady=(20, 10))
        for service in SERVICES:
            [name, price] = service
            service_variable = tk.StringVar()
            self.services_entry.append(service_variable)

            cb = ttk.Checkbutton(left_container, text=name+', $'+str(price), variable=service_variable, onvalue=name, offvalue=None)
            cb.pack(anchor=W, padx=60, pady=3)

        ttk.Label(right_container, text='Enter your name').pack(anchor=W, padx=60, pady=(20, 10))
        self.name_entry = ttk.Entry(right_container, width=36)
        self.name_entry.pack(anchor=W, padx=60)

        ttk.Label(right_container, text='Enter your phone').pack(anchor=W, padx=60, pady=(20, 10))
        self.phone_entry = ttk.Entry(right_container, width=36)
        self.phone_entry.pack(anchor=W, padx=60)

        ttk.Label(right_container, text='Enter your email').pack(anchor=W, padx=60, pady=(20, 10))
        self.email_entry = ttk.Entry(right_container, width=36)
        self.email_entry.pack(anchor=W, padx=60)


    def render_footer(self, container):
        container.pack(side=BOTTOM, fill=X)
        ttk.Button(container, text='Back', command=lambda: self.parent.go_back()).pack(side=LEFT)
        ttk.Button(container, text='Next', command=lambda: self.go_next()).pack(side=RIGHT)


    def go_next(self):
        self.parent.booking.date = self.date_entry.entry.get()
        self.parent.booking.time = self.time_entry.get_time()
        self.parent.booking.name = self.name_entry.get()
        self.parent.booking.phone = self.phone_entry.get()
        self.parent.booking.email = self.email_entry.get()
        self.parent.booking.services = []
        for entry in self.services_entry:
            service = entry.get()
            if service is not None and service != '':
                self.parent.booking.services.append(self._lookup_service_by_name(service))

        self.parent.go_next()


    def _lookup_service_by_name(self, name):
        for service in SERVICES:
            if service[0] == name:
                return service
        return None
