#Universidade Federal do Amazonas-UFAM
#aluna:  Ingrid de Lira Lima
#matricula: 21456913
#data: 30/06/2016

from math import*
X= int(input("digite seis digitos:"))
v1 = X // 1000
v2= X % 1000
dif= (v1-v2)

if(dif ** 2 == X):
	print(X," atende a propriedade")
else:
	print(dif ** 2)

