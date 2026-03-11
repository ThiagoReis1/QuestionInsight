from numpy import *
vetor=array(eval(input("quatro notas")))
vetor=sort(vetor)
soma=(vetor[0])+(vetor[1])+(vetor[2])
media=soma/3
media=round(media,2)
print(media)
if media >= 50.0:
	print("APROVADO")
else:
	print("REPROVADO")