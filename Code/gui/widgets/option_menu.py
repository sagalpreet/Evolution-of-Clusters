from ..utils import tk, Alignment
from .widget import Widget


class OptionMenu(Widget):

    tk_object = None
    tk_variable = None

    def __init__(self, values, selected_index=0, hidden=False, callback=None):
        assert len(values) > 0, "Provide at least one value for OptionsMenu"
        assert len(values) > selected_index >= 0, "Selected index out of bounds"
        super().__init__(hidden=hidden)
        self.values = values
        self.selected_index = selected_index
        self.callback = callback

    def __make_callback(self):
        if self.callback:
            self.callback(*self.get_value())

    def _initialize_tk_object(self, window):
        self.tk_variable = tk.StringVar(
            value=self.values[self.selected_index])
        self.tk_object = tk.OptionMenu(
            window, self.tk_variable, *self.values, command=lambda x: self.__make_callback())

    def get_value(self):
        if(self.tk_variable):
            selected_value = self.tk_variable.get()
            selected_index = -1
            for i in range(0, len(self.values)):
                if(self.values[i] == selected_value):
                    selected_index = i
                    break
            return (selected_index, selected_value)
        else:
            return self.selected_index, self.values[self.selected_index]
