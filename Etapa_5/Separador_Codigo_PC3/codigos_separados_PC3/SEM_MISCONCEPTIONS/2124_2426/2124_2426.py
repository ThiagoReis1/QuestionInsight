from numpy import *
notas = array(eval(input("notas: ")))
soma = sum(notas)
m = max(notas)
media = (soma - m)/3
if(media >= 5):
	print(round(media, 2))
	print("APROVOU")
else:
	print(round(media, 2))
	print("REPROVOU")