class Android():
	def __init__(self):
		self.apps = list()


	def installApp(self, app):
		self.apps.append(app)


	def unistallApp(self, app):
		if app in self.apps:
			self.apps.remove(app)