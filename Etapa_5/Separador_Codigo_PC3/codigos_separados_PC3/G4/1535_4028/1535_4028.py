# Entradas iniciais
from math import*
x = eval(input("valor do numero real x:"))
k = int(input("quantidade de termos da serie:"))

# Variaveis de Laço
soma = 0 # Variavel acumuladora
n = 0 # variavel contadora

while (n < k):
	soma = soma + ((-1)**n)*((x**(2*n+1))/(2*n+1))
	n = n + 1
# Saida do programa
print(round(soma,6))


