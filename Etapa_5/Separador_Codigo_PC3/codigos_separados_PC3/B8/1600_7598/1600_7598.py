from numpy import*

c = array(eval(input("custo dos itens: ")))
i = 0
total = 0

while(i<size(c)):
	if(c[i] >= 80):
		total = total - 15/100 * c[i] + c[i]
	elif(c[i] < 80):
		total = total + c[i]
	i = i + 1
print(round(total,2))

	
