from numpy import*

Y = array(eval(input("custo dos itens: ")))

i = 0
while(i < size(Y)):
	if(Y[i] > 80.0):
		Y[i] = Y[i] - 5.0
	i = i + 1
print(round(sum(Y), 2))