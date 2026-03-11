#Foundation by fenty beauty

from numpy import *

tom = input("tons: ").split(',')
saida = zeros(6, dtype=int)

for i in range(size(tom)):
	if(tom[i].upper() == "MC"):
		saida[0] = saida[0] + 1
	elif(tom[i].upper() == "C"):
		saida[1] = saida[1] + 1
	elif(tom[i].upper() == "CM"):
		saida[2] = saida[2] + 1
	elif(tom[i].upper() == "EM"):
		saida[3] = saida[3] + 1
	elif(tom[i].upper() == "E"):
		saida[4] = saida[4] + 1
	elif(tom[i].upper() == "ME"):
		saida[5] = saida[5] + 1

print(max(saida))
print(saida)
		
		
	