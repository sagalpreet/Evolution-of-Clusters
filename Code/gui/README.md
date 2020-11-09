## The basics
Import everything from `guimaker`
```python
from gui.guimaker import *
```
### How to create a widget?
- Creating a button
```python
def on_button_click():
	print("Button clicked!")

button = Button("Button Text", callback=on_button_click)
```

- Creating a slider
```python
def on_slider_change(value):
	print(f"Slider value changed to {value}!")

slider = Slider(0, 1, fractional=True, callback=on_slider_change)

# You can also find the value of slider with get_value()
print(slider.get_value())
```

- Adding some space
```python
space = Spacing(width=5, height=5)
```

### How to render these widgets
Simple! Lay them in a 2D array (grid) like you want to render them
```python
array = [
	[Spacing(5, 5)                      ],
	[Text('Text here'), None            ],
	[Button('One'),     Button('Two')   ],
	[Text('Threshold'), Slider(1, 10, 5)],
	[Spacing(5, 5)                      ],
]

create_gui(array, title='Some title')
```

### Just one more important widget
- `Grid`: It's takes a 2D array as input.
```python
grid1 = Grid([
	[Text('Wow'), Button('Nice')],
	[Text('Nice'), Button('Wow')]
])
grid2 = Grid([
	[Text('Good'), Button('Bad')],
	[Text('Bad'), Button('Good')]
])

create_gui([
	[grid1, grid2]
])
```

### Can I reuse the instance of a widget?
No
```python
button = Button('Hi')

create_gui([
	[button, button]
]) # This will create only one button
```

## Known Issues
1. `Spacing` does not work sometimes
2. `Slider.disable` not working
