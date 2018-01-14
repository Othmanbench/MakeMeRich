from Portfolio import *


p = Portfolio({})

p.addCoin("bitcoin", 1)
p.addCoin("ethereum", 5)
p.addCoin("litecoin",30)

p.showEvolution("Jan 01 2017", "Dec 30 2017")


q = Portfolio({})
q.investUSD("oyster-pearl", 100, "Dec 01 2017")
q.investUSD("elixir", 100, "Dec 01 2017")
q.investUSD("dent", 100, "Dec 01 2017")

q.showEvolution("Dec 01 2017", "Dec 30 2017")
