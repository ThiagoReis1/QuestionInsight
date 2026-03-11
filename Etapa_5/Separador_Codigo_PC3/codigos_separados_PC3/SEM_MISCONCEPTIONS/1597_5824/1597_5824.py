from numpy import *

valor=array(eval(input("Valor da compra: ")))
var=sum(valor)

for i in range(size(valor)):
	if valor[i]>80:
		var=var-5
	
print(var)
