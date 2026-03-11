#Julia Pacheco
#25 de Agosto de 2016
#Av 06 Ex02

from numpy import*
#ler um numero real
p = eval(input("p: "))
#ler vetor
x = array(eval(input("x: ")))
y = array(eval(input("y: ")))
#tamanho do vetor
n = size(x)
#valor de t
t = p/(p+1)
#variaveis de controle
i = 0
soma = 0.0
#calculo da norma
for i in range(n):
	soma = soma + (abs(x[i] - 2*(y[i])))**t
norma = soma**(1/t)
print(round(norma, 8))	
