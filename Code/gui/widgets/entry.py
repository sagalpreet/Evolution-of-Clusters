from ..utils import tk, Alignment
from .widget import Widget
import re


class Entry(Widget):

    tk_object = None
    tk_variable = None

    def __init__(self, text="", width=None, hidden=False, validator=None):
        super().__init__(hidden=hidden)
        self.text = text
        self.width = width
        self.validator = validator

    def _on_validate(self, final_text):
        if not self.validator or self.validator(final_text):
            return True
        else:
            return False

    def _initialize_tk_object(self, window):
        vcmd = (window.register(self._on_validate), '%P')
        self.tk_variable = tk.StringVar(value=self.text)
        self.tk_object = tk.Entry(window, textvariable=self.tk_variable,
                                  width=self.width, validate='key', validatecommand=vcmd)

    def get_value(self):
        if(self.tk_variable):
            return self.tk_variable.get()
        else:
            return self.text

class IntegerEntry(Entry):

    def __validator(self, text, negative_numbers_allowed):
        if not negative_numbers_allowed:
            regex = re.compile(r'^\d*$')
            if regex.match(text):
                return True
            else:
                return False
        else:
            regex = re.compile(r'^-?\d*$')
            if regex.match(text):
                return True
            else:
                return False
 
    def __init__(self, default_value=None, negative_numbers_allowed=True, width=None, hidden=False):
        self.default_value = 0 if default_value is None else int(default_value)
        super().__init__(text=str(self.default_value), width=width, hidden=hidden, validator=lambda text: self.__validator(text, negative_numbers_allowed))

    def get_value(self):
        text = super().get_value()
        try:
            return int(text)
        except:
            return self.default_value

class RealEntry(Entry):

    def __validator(self, text, negative_numbers_allowed):
        if not negative_numbers_allowed:
            regex = re.compile(r'^\d*(\.\d*)?$')
            if regex.match(text):
                return True
            else:
                return False
        else:
            regex = re.compile(r'^-?\d*(\.\d*)?$')
            if regex.match(text):
                return True
            else:
                return False
 
    def __init__(self, default_value=None, negative_numbers_allowed=True, width=None, hidden=False):
        self.default_value = float(0) if default_value is None else float(default_value)
        super().__init__(text=str(self.default_value), width=width, hidden=hidden, validator=lambda text: self.__validator(text, negative_numbers_allowed))

    def get_value(self):
        text = super().get_value()
        try:
            return float(text)
        except:
            return self.default_value
