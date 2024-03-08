import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.font as tkFont
from base_page import BasePage
from constants import *

#Class representing the third page of the application
class PageThree(BasePage):
    #Render the title section of the page
    def render_title(self, container):
        bold = tkFont.Font(family='Times', size=32)
        ttk.Label(container, text='Your Reservation Is Now Confirmed', font=bold, justify=LEFT).pack()

    #Render the body section of the page
    def render_body(self, container):
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)

        # Render booking details
        ttk.Label(container, text='Your name: ').grid(row=0, column=0, sticky=W, padx=60, pady=(0, 10))
        self.name_label = ttk.Label(container, text=self.parent.booking.name)
        self.name_label.grid(row=0, column=1, sticky=W, padx=60, pady=(0, 10))

        ttk.Label(container, text='Your phone: ').grid(row=1, column=0, sticky=W, padx=60, pady=(0, 10))
        self.phone_label = ttk.Label(container, text=self.parent.booking.phone)
        self.phone_label.grid(row=1, column=1, sticky=W, padx=60, pady=(0, 10))

        ttk.Label(container, text='Your email: ').grid(row=2, column=0, sticky=W, padx=60, pady=(0, 10))
        self.email_label = ttk.Label(container, text=self.parent.booking.email)
        self.email_label.grid(row=2, column=1, sticky=W, padx=60, pady=(0, 10))

        ttk.Label(container, text='Booking date: ').grid(row=3, column=0, sticky=W, padx=60, pady=(0, 10))
        self.date_label = ttk.Label(container, text=self.parent.booking.date)
        self.date_label.grid(row=3, column=1, sticky=W, padx=60, pady=(0, 10))

        ttk.Label(container, text='Booking time: ').grid(row=4, column=0, sticky=W, padx=60, pady=(0, 10))
        self.time_label = ttk.Label(container, text=self.parent.booking.time)
        self.time_label.grid(row=4, column=1, sticky=W, padx=60, pady=(0, 10))

        ttk.Label(container, text='Services: ').grid(row=5, column=0, sticky=W, padx=60, pady=(0, 10))
        self.services_container = ttk.Frame(container)
        self.services_container.grid(row=6, column=0, columnspan=2, sticky=W, padx=60, pady=(0, 10))
        self._clear_and_redraw_services()

    #Render the footer section of the page
    def render_footer(self, container):
        container.pack(side=BOTTOM, fill=X)
        ttk.Button(container, text='Back', command=lambda: self.parent.go_back()).pack(side=LEFT)
        ttk.Button(container, text='Exit', command=lambda: self.parent.destroy()).pack(side=RIGHT)

    #Refresh the displayed data
    def refresh_data(self):
        # Update displayed booking details
        self.name_label.config(text=self.parent.booking.name)
        self.phone_label.config(text=self.parent.booking.phone)
        self.email_label.config(text=self.parent.booking.email)
        self.date_label.config(text=self.parent.booking.date)
        self.time_label.config(text=self.parent.booking.time)
        self._clear_and_redraw_services()

    #Clear and redraw the list of services
    def _clear_and_redraw_services(self):
        # Clear existing services
        for widget in self.services_container.winfo_children():
            widget.destroy()

        # Draw services from the booking
        total = 0
        last_idx = 0
        for idx, service in enumerate(self.parent.booking.services or []):
            ttk.Label(self.services_container, text=" - "+service[0]+", $"+str(service[1])).grid(row=idx, column=0, sticky=W, padx=60, pady=(0, 10))
            total += service[1]
            last_idx = idx

        # Display total cost
        ttk.Label(self.services_container, text="------------Total: $"+str(total)).grid(row=last_idx+1, column=0, sticky=W, padx=60, pady=(0, 10))
