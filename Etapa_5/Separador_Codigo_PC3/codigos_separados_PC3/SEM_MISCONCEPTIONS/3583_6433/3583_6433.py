from numpy import *

item = array(eval(input("itens: ")))

i =0
total = 0

while i<size(item):
	if item[i] > 50:
		item[i] = item[i] - (item[i]*0.08)
	total += item[i]
	
	i += 1
print(round(total,2))