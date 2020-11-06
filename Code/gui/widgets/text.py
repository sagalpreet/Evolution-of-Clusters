from ..utils import tk, Alignment
from .widget import Widget


class Text(Widget):

    tk_object = None

    def __init__(self, text, width=None, height=None, hidden=False):
        super().__init__(hidden=hidden)
        self.text = text
        self.width = width
        self.height = height

    def _initialize_tk_object(self, window):
        self.tk_object = tk.Label(
            window, text=self.text, width=self.width, height=self.height)

    def get_text(self):
        return self.text
    
    def set_text(self, text):
        self.text = text
        if self.tk_object:
            self.tk_object['text'] = self.text
