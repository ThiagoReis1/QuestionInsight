from numpy import *
####################Entrada##################:
v = array(eval(input("Digite o vetor: ")))
cont = 0
##################For#########################:
for i in range(size(v)):
	cont = cont + ((v[i]**(1/3)))
cont = (cont/size(v))**3	
########################Print##################:
print(round(cont,2))