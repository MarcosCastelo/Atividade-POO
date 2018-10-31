from .view import View

class ViewGroup(View):
	def __init__(self):
		super().__init__()
		self.views = list()


	def isLayout(self):
		return False


	def addView(self, view):
		self.views.append(view)


	def removeView(self, view):
		if view in self.views:
			self.views.remove(view)