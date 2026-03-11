from numpy import *
notas = array(eval(input("Digite as três notas: ")))
media = (notas[0] * 5 + notas[1] * 3 + notas[2] * 2) / 10
print(round(media, 2))
if (media >= 5):
	print("APROVADO")
else:
	print("REPROVADO")