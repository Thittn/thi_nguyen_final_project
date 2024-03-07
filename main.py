import ttkbootstrap as ttk
from page_one import PageOne
from page_two import PageTwo
from page_three import PageThree
from constants import *

class Booking:

    def __init__(self, name='', phone='', email='', date=None, time='', services=[]):
        self.name = name
        self.phone = phone
        self.email = email
        self.date = date
        self.time = time
        self.services = services

class App(ttk.Window):
    page_order = 0

    def __init__(self):
        ttk.Window.__init__(self, title='Glow Nail Spa', themename='vapor', size=APP_SIZE)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.pages = []
        self.booking = Booking()
        for Page in [PageOne, PageTwo, PageThree]:
            self.pages.append(Page(parent=self))

        self.show_page()

    def show_page(self):
        page = self.pages[self.page_order]
        page.tkraise()

        # Call refresh_data method if it exists on the page
        refresh_data = getattr(page, "refresh_data", None)
        if callable(refresh_data):
            refresh_data()


    def go_back(self):
        self.page_order -= 1
        self.show_page()

    def go_next(self):
        self.page_order += 1
        self.show_page()

if __name__ == "__main__":
    app = App()
    app.mainloop()
