# File: page_two.py
# Author: Thi Nguyen
# Date: 03/08/2024
# Description: This file contains the implementation of the PageTwo class,
#              which represents the second page of the Glow Nail Spa Reservation System.
#              It includes functionality for rendering the title, body, and footer sections
#              of the page, allowing users to choose date, time, services, and enter personal
#              information for making a reservation. It also includes validation for user input
#              such as name, phone number, and email address


import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import DateEntry
import tkinter.font as tkFont
from base_page import BasePage
from time_picker import TimePicker
from constants import *

#Class representing the second page of the application
class PageTwo(BasePage):
    #Render the title section of the page
    def render_title(self, container):
        self.img = ttk.PhotoImage(file='fill_form.png', width=179, height=141)
        ttk.Label(container, image=self.img).pack()

        # Add and format welcome text to top of the page
        bold = tkFont.Font(family='Times', size=30)
        ttk.Label(container, text='Make Your Reservation Today', font=bold, justify=LEFT).pack()

    #Render the body section of the page
    def render_body(self, container):
        left_container = ttk.Frame(container)
        left_container.grid(row=0, column=0, sticky=W)
        right_container = ttk.Frame(container)
        right_container.grid(row=0, column=1, sticky=W)
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)

        # Render date and time selection
        ttk.Label(left_container, text='Choose date and time').pack(anchor=W, padx=60, pady=(0, 10))
        date_time_container = ttk.Frame(left_container)
        date_time_container.pack(anchor=W, padx=50)
        date_time_container.grid_columnconfigure(0, pad=20)
        self.date_entry = DateEntry(date_time_container)
        self.date_entry.grid(row=0, column=0)
        self.time_entry = TimePicker(date_time_container)
        self.time_entry.grid(row=0, column=1)
        self.services_entry = []

        # Render service selection
        ttk.Label(left_container, text='Choose services').pack(anchor=W, padx=60, pady=(20, 10))
        for service in SERVICES:
            [name, price] = service
            service_variable = tk.StringVar()
            self.services_entry.append(service_variable)

            cb = ttk.Checkbutton(left_container, text=name+', $'+str(price), variable=service_variable, onvalue=name, offvalue=None)
            cb.pack(anchor=W, padx=60, pady=3)

        # Render input fields for name, phone, and email
        ttk.Label(right_container, text='Enter your first name and last name').pack(anchor=W, padx=60, pady=(20, 10))
        self.name_entry = ttk.Entry(right_container, width=36)
        self.name_entry.pack(anchor=W, padx=60)

        ttk.Label(right_container, text='Enter your phone').pack(anchor=W, padx=60, pady=(20, 10))
        self.phone_entry = ttk.Entry(right_container, width=36)
        self.phone_entry.pack(anchor=W, padx=60)

        ttk.Label(right_container, text='Enter your email').pack(anchor=W, padx=60, pady=(20, 10))
        self.email_entry = ttk.Entry(right_container, width=36)
        self.email_entry.pack(anchor=W, padx=60)

        # Render error validation
        self.bottom_container = ttk.Frame(container)
        self.bottom_container.grid(row=1, column=0, columnspan=2, sticky=W, pady=(20,0))


    #Render the footer section of the page
    def render_footer(self, container):
        container.pack(side=BOTTOM, fill=X)
        ttk.Button(container, text='Back', command=lambda: self.parent.go_back()).pack(side=LEFT)
        ttk.Button(container, text='Confirm', command=lambda: self.go_next()).pack(side=RIGHT)

    #Go to next page
    def go_next(self):
        # Collect booking information from input fields and go to the next page
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

        if self._validate_form():
            self.parent.go_next()
        
        self._show_error()

    #Lookup service details by its name
    def _lookup_service_by_name(self, name):
        for service in SERVICES:
            if service[0] == name:
                return service
        return None


    #Validate data type
    def _validate_form(self):
        self.error = []

        # Validate name
        if not self.parent.booking.name or not self.parent.booking.name.strip():
            self.error.append('Please enter your name')

        # Validate phone number
        if not self.parent.booking.phone or not self.parent.booking.phone.strip():
            self.error.append('Please enter your phone number')
        elif not self._is_valid_phone(self.parent.booking.phone.strip()):
            self.error.append('Please enter a valid phone number')

        # Validate email
        if not self.parent.booking.email or not self.parent.booking.email.strip():
            self.error.append('Please enter your email')
        elif not self._is_valid_email(self.parent.booking.email.strip()):
            self.error.append('Please enter a valid email')

        # Validate booking time
        if not self.parent.booking.time or self.parent.booking.time == ':':
            self.error.append('Please select your booking time')

        # Validate selected services
        if not self.parent.booking.services:
            self.error.append('Please choose services to book')

        return len(self.error) == 0
   
    # Show error messages
    def _show_error(self):
        # Clear existing error
        for widget in self.bottom_container.winfo_children():
            widget.destroy()

        #Display new error message
        for err in self.error:
            ttk.Label(self.bottom_container, text=' - '+err, style=DANGER).pack(padx=60, anchor=W)


    # Helper method to validate phone number
    def _is_valid_phone(self, phone):
        return phone.isdigit() and len(phone) == 10

    # Helper method to validate email
    def _is_valid_email(self, email):
        import re
        email_format = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_format, email)