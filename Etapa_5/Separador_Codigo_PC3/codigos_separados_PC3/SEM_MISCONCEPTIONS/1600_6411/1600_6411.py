from numpy import *

cust = array(eval(input("Digite o valor: ")))
i = 0
total = 0

while i < size(cust):
	if cust[i] > 80.0:
		total = total + cust[i] * 0.85
	else:
		total = total + cust[i]
	i = i + 1
print(round(total, 2))
