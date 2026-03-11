from numpy import *

quantInfantaria = int(input("Entre com a quantidade inicial na infantaria: "))
quantCavalaria =  int(input("Entre com a quantidade inicial na cavalaria: "))
percentualI = float(input("Entre com o percentual na infantaria: "))
percentualC = float(input("Entre com o percentual na cavalaria: "))

meses = 0

while ((quantInfantaria + quantCavalaria) < 50000):
	quantInfantaria = quantInfantaria + (quantInfantaria * percentualI) / 100
	quantCavalaria = quantCavalaria + (quantCavalaria * percentualC) / 100
	meses = meses + 1
print(meses)
