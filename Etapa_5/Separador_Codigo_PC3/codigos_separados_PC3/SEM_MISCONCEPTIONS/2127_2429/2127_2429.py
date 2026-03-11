from numpy import*

nota = array(eval(input()))

media = ((sum(nota))-(min(nota)))/3

print(round(media,2))


if (media >= 50):
	print("APROVADO")
else:
	print("REPROVADO")
			
