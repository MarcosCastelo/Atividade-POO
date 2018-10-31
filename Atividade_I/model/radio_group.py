from .view_group import ViewGroup
from .radio_button import RadioButton 

class RadioGroup(ViewGroup):
	def addView(self, view):
		radio = type(view) is RadioButton
		if radio:
			super().addView(view)