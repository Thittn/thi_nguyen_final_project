import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.font as tkFont
from base_page import BasePage
from constants import *

#Class representing the first page of the application
class PageOne(BasePage):
    #Render the title section of the page
    def render_title(self, container):
        # Add and format image to top of the page
        self.img = ttk.PhotoImage(file='nail_spa.png', width=160, height=141)
        ttk.Label(container, image=self.img).pack()

        # Add and format welcome text to top of the page
        bold = tkFont.Font(family='Times', size=28)
        ttk.Label(container, text='Welcome to Glow Nail Spa', font=bold, justify=LEFT).pack()

    #Render the body section of the page
    def render_body(self, container):
        container.columnconfigure(0, weight=2)
        container.columnconfigure(1, weight=1)

        # Loop to format services in the left and cost in the right
        for i, (service, price) in enumerate(SERVICES):
            ttk.Label(container, text=service, justify=LEFT).grid(row=i, column=0, padx=self.GRID_PAD, pady=self.GRID_PAD, sticky=W)
            ttk.Label(container, text="$"+str(price), justify=RIGHT).grid(row=i, column=1, padx=self.GRID_PAD, pady=self.GRID_PAD, sticky=E)

    #Render the footer section of the page
    def render_footer(self, container):
        ttk.Button(container, text='Next', command=lambda: self.parent.go_next()).pack(side=RIGHT)
