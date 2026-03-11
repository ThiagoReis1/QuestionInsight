from numpy import *

saques = array(eval(input()))
cont_baixos = 0
list_pos = []

for i in range(size(saques)):
	 if saques[i] <= 50:
			cont_baixos = cont_baixos + 1
			list_pos.append(i)
			
print(cont_baixos)
print(array(list_pos))