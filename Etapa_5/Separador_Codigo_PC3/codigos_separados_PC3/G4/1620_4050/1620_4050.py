from numpy import *
x = array(eval(input("Digite o vetor tempo dos banhos: ")))
y = array(eval(input("Digite o vetor percentual da abertura da torneira: ")))

cont = 0
for i in range(size(x)):
	cont = cont + (x[i]*((y[i]/100)*5))
	
print(round(cont, 2))