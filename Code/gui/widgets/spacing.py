from ..utils import tk, Alignment
from .widget import Widget

class Spacing(Widget):

    tk_object = None

    def __init__(self, width, height, hidden=False):
        super().__init__(hidden=hidden)
        self.width = width
        self.height = height
    
    def _initialize_tk_object(self, window):
        self.tk_object = tk.Canvas(window, width=self.width, height=self.height)
