#Universidade Federal do Amazonas 
#Laís Amorim Reis - 21602327
from math import *

n = int(input("n: "))
numerador = 1
denominador = 3
i = 1
var = 0
while(i<=n):
	if(i==1):
		var = -1/9
	elif(i%2==0):
		var = var + (sqrt(numerador)/(6+denominador))
	else:
		var = var - (sqrt(numerador)/(6+denominador))
	i = i+1
	numerador = numerador + 1
	denominador = denominador + 2
print(round(var,5))