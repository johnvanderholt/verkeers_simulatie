from godot import exposed, export
from godot import *


@exposed
class Area(Area):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		pass
	
	def body_entered(self):
		print("entered")
		
	def _on_Area_body_entered(one, two):
		print("entered area2")

	def _on_Area_body_exited(one, two):
		print("entered area2")