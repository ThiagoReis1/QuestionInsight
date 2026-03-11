from numpy import*
notas = array(eval(input("Notas: ")))
media= (notas[0]*5+notas[1]*2.5+notas[2]*2.5)/10
print(round(media,2))
if media>=5:
	print("APROVADO")
else:
	print("REPROVADO")