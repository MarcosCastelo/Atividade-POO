from .button import Button 

class RadioButton(Button):
	def __init__(self):
		super().__init__()
		self.marked = False


	def mark(self):
		self.marked = True

	def dismark(self):
		self.marked = False