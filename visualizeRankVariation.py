import matplotlib.pyplot as plt
from computeVariation import *

#visualize the variation distribution depending on rank for a size
#Ex : visualizeRankVariations("Jan 01 2017", "Jan 30 2017", 50)
def visualizeRankVariations(initialDate, finalDate, nbCoins, totalCoinsNb):
	x = range(0, totalCoinsNb, nbCoins)
	variations = allCoinsVariations(initialDate, finalDate)
	print(len(list(variations.values())))

	values = [moyenne(i,i+nbCoins) for i in x]

	plt.bar(x, values)
	plt.show()


visualizeRankVariations("Dec 01 2017", "Dec 30 2017", 1, 850)

