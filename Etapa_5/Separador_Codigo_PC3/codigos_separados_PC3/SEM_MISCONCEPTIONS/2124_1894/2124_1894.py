from numpy import *

notas = array(eval(input("digite: ")))
x = max(notas)

media = (sum(notas) - x)/3

print(round(media,2))

if (media >= 5.0):
	print("APROVOU")
else:
	print("REPROVOU")
