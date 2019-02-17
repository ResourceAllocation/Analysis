from Testing import Testing
if __name__ == '__main__':
	TestObject=Testing()
	TestObject.Split_status()
	TestObject.CalculateDelivery()
	TestObject.PrintDelivery(0)
	TestObject.PrintDelivery(1)
	TestObject.PrintDelivery(2)
	TestObject.plotDelivery(0)
	TestObject.plotDelivery(1)
	TestObject.plotDelivery(2)