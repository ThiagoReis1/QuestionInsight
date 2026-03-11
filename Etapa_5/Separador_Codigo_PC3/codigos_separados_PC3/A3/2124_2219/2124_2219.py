from numpy import*

notas = array(eval(input("Informe as notas:")))
i = 0
media = (notas[0]+ notas[1]+notas[2]+notas[3]- max(notas))/3
if (media >= 5.0):
	
	print(round(media,2))
	print("APROVOU")
else:
	print(round(media,2))
	print("REPROVOU")	