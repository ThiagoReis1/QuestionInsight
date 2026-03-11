from numpy import*
v = array(eval(input("Digite o custo dos itens:")))
i = 0
total = 0

while(i < size(v)):
	if(i > 80.00):
		d = 5.00
		total = total + v - d
	else:
		total = total + v
	i = i + 1
	
print(round(total,2))
