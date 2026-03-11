from numpy import*

custo = array(eval(input("custo de itens:")))
c = 0
total = sum(custo)

while (c < size(custo)):
	a = custo[c]
	c = c + 1
	if (a >= 80): 
		total = total - 5

print(round(total, 2))
		

		

	

	


