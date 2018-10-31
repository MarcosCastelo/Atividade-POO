from .view_group import ViewGroup 

class Activity():
	def __init__(self):
		self.layout = ViewGroup()


	def setContetLayout(self, viewGroup):
		if viewGroup.isLayout():
			self.layout = viewGroup
