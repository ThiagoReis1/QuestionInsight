from math import *
p = float(input("Digite o valor do patrimonio da Pobresco: "));
b = float(input("Digite o valor do patrimonio da Bitcoin : "));
pp = float(input("Digite o valor do percentual de crescimento da Pobresco: "));
pb = float(input("Digite o valor do percentual de crescimento da Bitcoin: "));
ap = p + p * pp / 100
ab = b + b * pb / 100
qp = 0
qb = 0
y = 1
while(qb <= qp):
	qp = ap + qp
	qb = ab + qb
	y = y + 1
while(qb > qp):
	print(y)
