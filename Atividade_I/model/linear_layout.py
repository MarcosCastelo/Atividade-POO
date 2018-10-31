from .view_group import ViewGroup

class LinearLayout(ViewGroup):
	def __init__(self, orientation):
		super().__init__()
		self.orientation = orientation


	def isLayout(self):
		return True