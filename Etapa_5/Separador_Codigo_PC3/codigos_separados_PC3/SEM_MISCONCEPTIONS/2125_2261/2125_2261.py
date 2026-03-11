from numpy import *
nota = array(eval(input(":")))

media = (nota[0] * 3+ nota[1]*3 + nota[2]*4)/10
print(round(media, 2))
if(media>=5):
	print("APROVADO")
else:
	print("REPROVADO")