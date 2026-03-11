#--------------------------------------------------
#Universidade Federal do Amazonas
#Larisse Gabriele Ramos de Abreu
#Data: 21/12/2016
#
#Objetivo: Serie de Maclaurin do Arco Tangente
#---------------------------------------------------
from math import*

x = eval(input("Um numero real x: "))
n = eval(input("A quantidade de termos da serie: "))

k =  1
valor = 1
qo = x

while(k < n ):
	x = x - (((qo)**((2 * k) + 1 ))/((2 * k) + 1))
	qo = - qo
	k = k + 1 
print(round(x, 6))
	

