import ttkbootstrap as ttk
from page_one import PageOne
from page_two import PageTwo
from page_three import PageThree
from constants import *

#Class for booking details
class Booking:
    #Initialize attribites for booking class
    def __init__(self, name='', phone='', email='', date=None, time='', services=[]):
        self.name = name
        self.phone = phone
        self.email = email
        self.date = date
        self.time = time
        self.services = services

#Class for main application
class App(ttk.Window):
    #Initialize page order as 0
    page_order = 0
    #Initialize the App class inheriting from ttk.Window
    def __init__(self):
        ttk.Window.__init__(self, title='Glow Nail Spa Reservation System', themename='vapor', size=APP_SIZE)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #List to store instances of pages
        self.pages = []
        #Initialize booking details
        self.booking = Booking()
        #Loop through page classes and append instances to self.pages list
        for Page in [PageOne, PageTwo, PageThree]:
            self.pages.append(Page(parent=self))

        #Show the initial page
        self.show_page()

    #Show the current page based on page_order
    def show_page(self):
        page = self.pages[self.page_order]
        page.tkraise()

        # Call refresh_data method if it exists on the page
        refresh_data = getattr(page, "refresh_data", None)
        if callable(refresh_data):
            refresh_data()

    #Go to the previous page
    def go_back(self):
        self.page_order -= 1
        self.show_page()

    #Go to next page
    def go_next(self):
        self.page_order += 1
        self.show_page()

if __name__ == "__main__":
    #Create an instance of the App class
    app = App()
    app.mainloop()
