from .view import View

class TextView(View):
	def __init__(self):
		super().__init__()
		self.text = "Hello World!"


	def setText(self, text):
		self.text = text
