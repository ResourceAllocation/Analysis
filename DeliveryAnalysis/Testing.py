from TestingDelivery import TestingDelivery
from TestingInterface import TestInterface
class Testing(TestingDelivery,TestInterface):
	"""docstring for Tesing"""
	def __init__(self):   # Parsing tha data into file 
		TestingDelivery.__init__(self)
		TestInterface.__init__(self)

	def CalculateDelivery(self):
		TestInterface.CountDeliveredSent(self)
		
		