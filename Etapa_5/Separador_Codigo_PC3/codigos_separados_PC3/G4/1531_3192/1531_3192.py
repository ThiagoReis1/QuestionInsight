from math import * 
ang = eval(input("digite um angulo: "))
k = int(input("digite a quantidade de repeticoes: "))

cont = 1
soma = 1

while(cont < k):
	soma = soma + ((-1)**(cont) * (ang)**(cont * 2)) / factorial(cont * 2)
	cont = cont + 1
	
print(round(soma, 10))