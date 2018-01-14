def removeZerosFromEnd(line):
	end = len(line)-1

	i = end
	while(line[i] == 0 and i>-1):
		i=i-1

	if i == -1:
		print("FUCK")
		return None

	i = i+1

	count = 0
	while(i<=end and count <3):
		count = count+1
		line[i] = line[i-1]

	return line

def fillBetween(line, first0, last0):
	print("filling")
	zerosNb = last0 - first0+1

	toAdd = (line[last0+1] - line[first0-1])/(zerosNb+1)

	for i in range(first0, last0 +1):
		print("filling mziannnn")
		line[i] = line[i-1]+toAdd

	return line

def replaceZeros(line):

	i = 0
	while(i<len(line) and line[i] == 0):
		i=i+1

	if i<len(line):
		while ( i<len(line) and line[i]>0):
			i=i+1

		if i==len(line):
			return line

		first0 = i
		while(i<len(line) and line[i]==0):
			i=i+1

		if i==len(line):
			return removeZerosFromEnd(line)

		last0 = i-1

		if first0!=last0 + 1 :
			line = fillBetween(line, first0, last0)
			return replaceZeros(line)
		else:
			return line

	else:
		return line

def coinMarketCap (table,coinRank,date):
	return table[coinRank-1][date-1]

def coinVariation(table, coinRank, initialDate, finalDate):

	if table[initialDate-1] == 0:
		print("coin was not there")
		return None
	
	initialMarketCap = 0
	i=0
	while (initialMarketCap==0 and i<finalDate-initialDate +1):
	 	initialMarketCap = coinMarketCap (table, coinRank, initialDate+i)
	 	i=i+1
	if initialMarketCap == 0:
		variationPercentage = 0
	else:
		finalMarketCap	= coinMarketCap (table, coinRank, finalDate)
		if finalMarketCap == 0:
			variationPercentage= -100
		else:
			variationPercentage = 100*(finalMarketCap - initialMarketCap)/initialMarketCap

	return variationPercentage

def listCoinsVariation(table, initialCoinRank, nbCoins, intialDate, finalDate):
	average = 0
	finalCoinRank = nbCoins + initialCoinRank - 1
	for i in range (initialCoinRank,finalCoinRank+1):
		average = average + coinVariation(table,i,intialDate,finalDate) / nbCoins

	return average

# for i in range(5,7):
# 	print(i)

# toto = {}
# toto["btc"] = 1
# toto["ltc"] = 2 
# toto["eth"] = 3
# toto["xxx"] = 4
# print(toto.values())



def moyenne (i, j) :
	somme = 0
	listvariations = list(variations.values())
	for k in range(i,j):
		somme = somme + listvariations[k]

	return somme/(j-i)

def allCoinsVariations(initialDate, finalDate):
	global variations
	variations = {}

	initialMarketCap, finalMarketCap = {},{}

	with open("dates/" + initialDate + ".txt") as initialDateFile :
		with open("dates/" + finalDate + ".txt") as finalDateFile :
			for line in initialDateFile:
				data = line.split(";")
				if float(data[6]) != 0:
					initialMarketCap[data[0]] = float(data[6])

			for line in finalDateFile:
				data = line.split(";")
				finalMarketCap[data[0]] = float(data[6])

			for key in initialMarketCap.keys():
				if key in finalMarketCap.keys() :
					variations[key] = finalMarketCap[key] / initialMarketCap[key]

	return variations

def getA7ssanBhadLaTaille(initialDate, finalDate, taille):
	# initialmarketcap =1 finalmarketcap =2: multiplicativeValue= 2
	multiplicationValue = -1

	bestStartingIndex = -1
	moyennes = []

	variations = allCoinsVariations(initialDate, finalDate)

	for i in range(len(variations)-taille):
		moyennes.append(moyenne(i,i+taille))

	for i in range(len(moyennes)):
		if moyennes[i] > multiplicationValue :
			multiplicationValue = moyennes[i]
			bestStartingIndex = i

	return bestStartingIndex+2,multiplicationValue

#print(getA7ssanBhadLaTaille("Jan 06 2017", "Jan 07 2017", 10))

#best nbrOfCoins between 20 and 50 in given dates

def bestGivenPastDates(initialDate,finalDate,initialSize,finalSize):
	
	bestList = []
	bestSize = -1
	index = -1
	bestElement = []

	for i in range(initialSize,finalSize):
		
		#bestWithSizei = [bestIndex, multiplicationValue, size]
		bestWithSizei= []

		bestWithSizei= list(getA7ssanBhadLaTaille(initialDate, finalDate, i))
		bestWithSizei.append(i)

		bestList.append(bestWithSizei)


	for elt in bestList:
		if elt[1] > bestSize:
			bestElement = elt
			bestSize = elt[1]

	return bestElement

#print(bestGivenPastDates("Jan 14 2017", "Jan 20 2017",20, 50))

# best index for a given number of days
# we how to define periods in the year: from date1 to date2 period is 


dates = ['Dec 31 2017','Dec 30 2017','Dec 29 2017','Dec 28 2017','Dec 27 2017','Dec 26 2017','Dec 25 2017','Dec 24 2017','Dec 23 2017','Dec 22 2017','Dec 21 2017','Dec 20 2017','Dec 19 2017','Dec 18 2017','Dec 17 2017','Dec 16 2017','Dec 15 2017','Dec 14 2017','Dec 13 2017','Dec 12 2017','Dec 11 2017','Dec 10 2017','Dec 09 2017','Dec 08 2017','Dec 07 2017','Dec 06 2017','Dec 05 2017','Dec 04 2017','Dec 03 2017','Dec 02 2017','Dec 01 2017','Nov 30 2017','Nov 29 2017','Nov 28 2017','Nov 27 2017','Nov 26 2017','Nov 25 2017','Nov 24 2017','Nov 23 2017','Nov 22 2017','Nov 21 2017','Nov 20 2017','Nov 19 2017','Nov 18 2017','Nov 17 2017','Nov 16 2017','Nov 15 2017','Nov 14 2017','Nov 13 2017','Nov 12 2017','Nov 11 2017','Nov 10 2017','Nov 09 2017','Nov 08 2017','Nov 07 2017','Nov 06 2017','Nov 05 2017','Nov 04 2017','Nov 03 2017','Nov 02 2017','Nov 01 2017','Oct 31 2017','Oct 30 2017','Oct 29 2017','Oct 28 2017','Oct 27 2017','Oct 26 2017','Oct 25 2017','Oct 24 2017','Oct 23 2017','Oct 22 2017','Oct 21 2017','Oct 20 2017','Oct 19 2017','Oct 18 2017','Oct 17 2017','Oct 16 2017','Oct 15 2017','Oct 14 2017','Oct 13 2017','Oct 12 2017','Oct 11 2017','Oct 10 2017','Oct 09 2017','Oct 08 2017','Oct 07 2017','Oct 06 2017','Oct 05 2017','Oct 04 2017','Oct 03 2017','Oct 02 2017','Oct 01 2017','Sep 30 2017','Sep 29 2017','Sep 28 2017','Sep 27 2017','Sep 26 2017','Sep 25 2017','Sep 24 2017','Sep 23 2017','Sep 22 2017','Sep 21 2017','Sep 20 2017','Sep 19 2017','Sep 18 2017','Sep 17 2017','Sep 16 2017','Sep 15 2017','Sep 14 2017','Sep 13 2017','Sep 12 2017','Sep 11 2017','Sep 10 2017','Sep 09 2017','Sep 08 2017','Sep 07 2017','Sep 06 2017','Sep 05 2017','Sep 04 2017','Sep 03 2017','Sep 02 2017','Sep 01 2017','Aug 31 2017','Aug 30 2017','Aug 29 2017','Aug 28 2017','Aug 27 2017','Aug 26 2017','Aug 25 2017','Aug 24 2017','Aug 23 2017','Aug 22 2017','Aug 21 2017','Aug 20 2017','Aug 19 2017','Aug 18 2017','Aug 17 2017','Aug 16 2017','Aug 15 2017','Aug 14 2017','Aug 13 2017','Aug 12 2017','Aug 11 2017','Aug 10 2017','Aug 09 2017','Aug 08 2017','Aug 07 2017','Aug 06 2017','Aug 05 2017','Aug 04 2017','Aug 03 2017','Aug 02 2017','Aug 01 2017','Jul 31 2017','Jul 30 2017','Jul 29 2017','Jul 28 2017','Jul 27 2017','Jul 26 2017','Jul 25 2017','Jul 24 2017','Jul 23 2017','Jul 22 2017','Jul 21 2017','Jul 20 2017','Jul 19 2017','Jul 18 2017','Jul 17 2017','Jul 16 2017','Jul 15 2017','Jul 14 2017','Jul 13 2017','Jul 12 2017','Jul 11 2017','Jul 10 2017','Jul 09 2017','Jul 08 2017','Jul 07 2017','Jul 06 2017','Jul 05 2017','Jul 04 2017','Jul 03 2017','Jul 02 2017','Jul 01 2017','Jun 30 2017','Jun 29 2017','Jun 28 2017','Jun 27 2017','Jun 26 2017','Jun 25 2017','Jun 24 2017','Jun 23 2017','Jun 22 2017','Jun 21 2017','Jun 20 2017','Jun 19 2017','Jun 18 2017','Jun 17 2017','Jun 16 2017','Jun 15 2017','Jun 14 2017','Jun 13 2017','Jun 12 2017','Jun 11 2017','Jun 10 2017','Jun 09 2017','Jun 08 2017','Jun 07 2017','Jun 06 2017','Jun 05 2017','Jun 04 2017','Jun 03 2017','Jun 02 2017','Jun 01 2017','May 31 2017','May 30 2017','May 29 2017','May 28 2017','May 27 2017','May 26 2017','May 25 2017','May 24 2017','May 23 2017','May 22 2017','May 21 2017','May 20 2017','May 19 2017','May 18 2017','May 17 2017','May 16 2017','May 15 2017','May 14 2017','May 13 2017','May 12 2017','May 11 2017','May 10 2017','May 09 2017','May 08 2017','May 07 2017','May 06 2017','May 05 2017','May 04 2017','May 03 2017','May 02 2017','May 01 2017','Apr 30 2017','Apr 29 2017','Apr 28 2017','Apr 27 2017','Apr 26 2017','Apr 25 2017','Apr 24 2017','Apr 23 2017','Apr 22 2017','Apr 21 2017','Apr 20 2017','Apr 19 2017','Apr 18 2017','Apr 17 2017','Apr 16 2017','Apr 15 2017','Apr 14 2017','Apr 13 2017','Apr 12 2017','Apr 11 2017','Apr 10 2017','Apr 09 2017','Apr 08 2017','Apr 07 2017','Apr 06 2017','Apr 05 2017','Apr 04 2017','Apr 03 2017','Apr 02 2017','Apr 01 2017','Mar 31 2017','Mar 30 2017','Mar 29 2017','Mar 28 2017','Mar 27 2017','Mar 26 2017','Mar 25 2017','Mar 24 2017','Mar 23 2017','Mar 22 2017','Mar 21 2017','Mar 20 2017','Mar 19 2017','Mar 18 2017','Mar 17 2017','Mar 16 2017','Mar 15 2017','Mar 14 2017','Mar 13 2017','Mar 12 2017','Mar 11 2017','Mar 10 2017','Mar 09 2017','Mar 08 2017','Mar 07 2017','Mar 06 2017','Mar 05 2017','Mar 04 2017','Mar 03 2017','Mar 02 2017','Mar 01 2017','Feb 28 2017','Feb 27 2017','Feb 26 2017','Feb 25 2017','Feb 24 2017','Feb 23 2017','Feb 22 2017','Feb 21 2017','Feb 20 2017','Feb 19 2017','Feb 18 2017','Feb 17 2017','Feb 16 2017','Feb 15 2017','Feb 14 2017','Feb 13 2017','Feb 12 2017','Feb 11 2017','Feb 10 2017','Feb 09 2017','Feb 08 2017','Feb 07 2017','Feb 06 2017','Feb 05 2017','Feb 04 2017','Feb 03 2017','Feb 02 2017','Feb 01 2017','Jan 31 2017','Jan 30 2017','Jan 29 2017','Jan 28 2017','Jan 27 2017','Jan 26 2017','Jan 25 2017','Jan 24 2017','Jan 23 2017','Jan 22 2017','Jan 21 2017','Jan 20 2017','Jan 19 2017','Jan 18 2017','Jan 17 2017','Jan 16 2017','Jan 15 2017','Jan 14 2017','Jan 13 2017','Jan 12 2017','Jan 11 2017','Jan 10 2017','Jan 09 2017','Jan 08 2017','Jan 07 2017','Jan 06 2017','Jan 05 2017','Jan 04 2017','Jan 03 2017','Jan 02 2017','Jan 01 2017']

btcUpResultsInAltsDown = dates[0:1]
btcUpAndAltsStable = dates[0:1]
btcUpResultsInAltsUp = dates[0:1]
btcStableResultsInAltsDown = dates[0:1]
AllStable = dates[20:34]
btcStableAndAltsUp = dates[0:1]
btcDownResultsInAltsDown = dates[0:1]
btcDownAndAltsStable = dates[0:1]
btcDownResultsInAltsUp = dates[0:1]

# periods = [btcUpResultsInAltsDown, btcUpAndAltsStable, btcUpResultsInAltsUp, btcStableResultsInAltsDown, AllStable, btcStableAndAltsUp, btcDownResultsInAltsDown, btcDownAndAltsStable, btcDownResultsInAltsUp]


def periodTypeGivenDate(date):
	
	periodType = AllStable
	#study past week fluctuation

	return periodType

def bestGivenFutureDates(initialDate, finalDate):

	bestElement = []

	dateRange = periodTypeGivenDate(initialDate)

	bestElement = bestGivenPastDates(dateRange[0], dateRange[len(dateRange)-1] , 10, 100)

	return bestElement

#print(bestGivenFutureDates("dateeee", "dateeeee"))

# f = open('datakkk.csv', 'r')

# content = f.readlines()

# tableZeros = [list(map(float, line.split(";")[1:len(line.split(";"))-1])) for line in content[1:]]

# table = list(map(replaceZeros, tableZeros))

# open('data1.txt', 'w').write(str(table))

# def averageRankandVariation
# best = []
# for i in range(1,31):
# 	j= i+1
# 	j= str(j).zfill(2)
# 	i=str(i).zfill(2)
# 	best.append(list(getA7ssanBhadLaTaille("Nov "+i+ " 2017", "Nov "+ j+ " 2017", 50)))

# average = 0
# summ = 0
# summ1 = 0
# rank = []


# for k in range(len(best)):
# 	rank = best[k]
# 	summ = summ + rank[0]
# 	summ1 = summ1 + rank[1]

# averageRank = summ/ 30
# averageVariation = summ1/30

# print(averageRank,averageVariation)
