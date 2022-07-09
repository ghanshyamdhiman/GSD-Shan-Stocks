from GSDStocks import GSDStock

print('start')
sn = 'SBIN.NS'
g1 = GSDStock(sn)

sp = g1.getStockPrice()
print("Curent Stock Price", sp)

pc = g1.getPreviousClosePrice()
print("Previous Close ", pc)

hd = g1.getStockHistoy()
print(hd)

hdc = g1.getStockHistoyCols()
print(hdc)

gr = g1.getGraph()

col_name = hd.columns

print(col_name)

print(type(hdc))

print('end')

