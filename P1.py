class Computer():
	def __init__(self):
		self.__maxprice=1000
	def sell(self):
		print("Selling prince: {}".format(self.__maxprice))
	def setMaxPrice(self,price):
		self.__maxprice=price
c=Computer()
c.sell()
c.__maxprice=900
c.sell()
c.setMaxPrice(900)
c.sell()