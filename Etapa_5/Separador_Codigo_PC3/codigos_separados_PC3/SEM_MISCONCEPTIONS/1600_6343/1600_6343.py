from numpy import *
itens = array(eval(input("itens: ")))
i = 0
s = 0
while i < size(itens):
	if itens[i] > 80.0:
		total = itens[i] - (15/100*itens[i])
		s = s + total
	else:
		total = itens[i]
		s = s + total
	i = i + 1
print(round(s,2))