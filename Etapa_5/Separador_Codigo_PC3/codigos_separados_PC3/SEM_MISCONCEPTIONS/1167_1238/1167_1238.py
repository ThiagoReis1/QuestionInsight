# Talita Oliveira Gomes Passos
# 28 de Julho de 2016
# Av. 4 - Ex 02

from math import *

N = int(input("Digite um número inteiro: "))

#Var contadora
count = 7

#Var acumuladora
acum = 1 

while(N > 0):
	serie = pow(acum, 2)/ count + 3 
print(serie)
	