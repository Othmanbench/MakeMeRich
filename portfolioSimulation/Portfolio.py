import os
import matplotlib.pyplot as plt
import datetime


class Portfolio:
	def __init__(self, coins = {}):
		# coins is a map associating each coin name to its amount in the portfolio.
		#Ex : coins = {"bitcoin" : 1.5, "ethereum" : 3,"litecoin" : 10}
		self.coins = coins

	#adds an amount of a coin to the portfolio
	def addCoin(self, coinName, amount):
		if coinName in self.coins.keys():
			self.coins[coinName] = self.coins[coinName] + amount
		else :
			self.coins[coinName] = amount

	#adds usdAmount worth of coinName at date (price = open price).
	#Ex : p.investUSD("monero", 500, "Nov 20 2017")
	def investUSD(self, coinName, usdAmount, date):
		file = open(os.path.abspath(__file__ + "/../../data/"+coinName+".txt"), "r")
		lines = file.readlines()
		for line in lines:
			lineData = line.split(";")
			if date == lineData[0] :
				self.addCoin(coinName, usdAmount/float(lineData[1]))
				return
		raise ValueError("cannot retrieve coin info from " +os.path.abspath(__file__ + "/../../data/"+coinName+".txt"))

	#returns the portfolio usd value at date.
	#Ex : p.getTotalUSD("Dec 30 2017")
	def getTotalUSD(self, date):
		total = 0
		data = open(os.path.abspath(__file__ + "/../../dates/"+date+".txt"), "r").readlines()

		for coin,amount in self.coins.items():
			for line in data :
				lineData = line.split(";")
				if(lineData[0] == coin):
					total = total + float(lineData[1])*self.coins[coin]
		return total

	def showEvolution(self, beginDate, endDate):
		monthToNb = {"Jan" : 1,"Feb" : 2,"Mar" : 3,"Apr" : 4,"May" : 5,"Jun" : 6,"Jul" : 7,"Aug" : 8,"Sep" : 9,"Oct" : 10,"Nov" : 11,"Dec" : 12}
		nbToMonth = dict((v,k) for k,v in monthToNb.items())
		splittedBegin = beginDate.split()
		splittedEnd = endDate.split()
		begin = datetime.date(int(splittedBegin[2]), monthToNb[splittedBegin[0]], int(splittedBegin[1]))
		end = datetime.date(int(splittedEnd[2]), monthToNb[splittedEnd[0]], int(splittedEnd[1]))

		period = [begin + datetime.timedelta(days=i) for i in range((end-begin).days)]
		values = [self.getTotalUSD(nbToMonth[(period[i]).month]+" "+str((period[i]).day).zfill(2)+" "+str((period[i]).year)) for i in range((end-begin).days)]

		plt.plot(period, values)
		plt.show()

