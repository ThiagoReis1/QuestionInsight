from numpy import *

notas = array(eval(input("Notas: ")))
pesos = [3.0, 2.0, 2.0, 3.0]

i = 0
soma = 0

while i < size(notas):
	soma = soma + notas[i]*pesos[i]
	i = i + 1
	
media = round(soma / 10, 2)

print(media)
if(media >= 5):
	print("APROVADO")
else:
	print("REPROVADO")