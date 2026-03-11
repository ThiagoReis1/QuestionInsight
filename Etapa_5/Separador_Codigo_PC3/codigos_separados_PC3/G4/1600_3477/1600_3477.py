from numpy import*
v = array(eval(input("custo dos itens: ")))
i = 0
while(i > v):
	if(v > 80):
		v = v - (v * 15/100)
		i = i +1
print(round(v,2))	