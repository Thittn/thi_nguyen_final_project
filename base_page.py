import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from constants import *

class BasePage(ttk.Frame):
    #Initialize values for grid pad and title pad
    GRID_PAD = 4
    TTTLE_PAD = 20

    def __init__(self, parent):
        # Create a frame for the page and pack it into the parent with the grid layout sticky to all sides
        ttk.Frame.__init__(self, parent)
        self.grid(row=0, column=0, sticky='news')
        self.parent = parent
        self.render()

    def render(self):
        # Create a frame for the title
        self.top_container = ttk.Frame(self, padding=PAGE_PAD)
        self.top_container.pack(side=TOP, fill=X, pady=10)
        self.render_title(self.top_container)

        # Create a frame for the body
        self.body_container = ttk.Frame(self, padding=PAGE_PAD)
        self.body_container.pack(fill=X)
        self.render_body(self.body_container)

        self.footer_container = ttk.Frame(self, style='light',  padding=PAGE_PAD)
        self.footer_container.pack(side=BOTTOM, fill=X)
        self.render_footer(self.footer_container)

    def render_title(self):
        # Subclasses should override this method
        pass

    def render_body(self):
        # Subclasses should override this method
        pass

    def render_footer(self):
        # Subclasses should override this method
        pass
