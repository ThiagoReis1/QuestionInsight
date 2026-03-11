from numpy import *
x = array(eval(input("DIgite os coeficientes: ")))
saida = ""
i = 0
g = size(x) -1	
while i <  size(x)-2:
	saida = saida + str(x[i]) + "x^"+ str(g) + " + " 
	i = i + 1
	g = g -1
saida = saida + str(x[i]) + "x + " +str(x[i+1])
print(saida)
