from .view_group import ViewGroup 

class ScrollView(ViewGroup):

	def addView(self, view):
		limit = len(self.views) > 0

		if not limit:
			super().addView(view)
