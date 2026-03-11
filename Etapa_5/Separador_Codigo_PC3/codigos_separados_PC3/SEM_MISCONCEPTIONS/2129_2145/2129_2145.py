from numpy import*
notas = array(eval(input("Digite as notas: ")))

media = (notas[0] + notas[1]*2 + notas[2]*3 + notas[3]*4)/10
print(round(media, 2))
if (media >= 5):
	print("APROVADO")
else:
	print("REPROVADO")