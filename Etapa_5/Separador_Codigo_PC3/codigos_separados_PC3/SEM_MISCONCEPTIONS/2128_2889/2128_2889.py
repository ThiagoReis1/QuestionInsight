from numpy import*

notas = array (eval(input ("Informe as Notas")))

maior = max(notas)

media = ((notas[0]+notas[1]+notas[2]+notas[3]) - maior)/3

if (media > 50.0):
	print (round(media,2))
	print ("APROVADO")
else: 
	print (round(media,2))
	print ("REPROVADO")