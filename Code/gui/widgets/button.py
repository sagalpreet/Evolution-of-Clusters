from ..utils import tk, Alignment
from .widget import Widget


class Button(Widget):

    def __init__(self, text, width=None, height=None, hidden=False, callback=None):
        super().__init__(hidden=hidden)
        self.text = text
        self.width = width
        self.height = height
        self.callback = callback

    def __make_callback(self):
        if(self.callback):
            self.callback()

    def _initialize_tk_object(self, window):
        self.tk_object = tk.Button(
                window, text=self.text, width=self.width, height=self.height, command=self.__make_callback)
