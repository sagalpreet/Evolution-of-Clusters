from ..utils import tk, Alignment
from .widget import Widget

class ListBox(Widget):

    tk_object = None

    def __init__(self, values, selected_index=0, width=None, height=None, hidden=False):
        assert len(values)>0, "Provide at least one value for OptionsMenu"
        assert len(values)>selected_index>=0, "Selected index out of bounds"
        super().__init__(hidden=hidden)
        self.values = values
        self.selected_index = selected_index
        self.width = width
        self.height = height

    def _initialize_tk_object(self, window):
        self.tk_object = tk.Listbox(window, width= self.width, height=self.height)
        for i in range(len(self.values)):
            self.tk_object.insert(i+1, self.values[i])
        self.tk_object.select_set(self.selected_index)

    def get_value(self):
        if(self.tk_object):
            selected_index = self.tk_object.curselection()[0]
            selected_value = self.values[selected_index]
            return selected_index, selected_value
        else:
            return self.selected_index, self.values[selected_value]
