from numpy import *

vetor = array(eval(input("Entre com o vetor: ")))

media = (sum(vetor) - max(vetor)) / 3.0
print(round(media, 2))

if (media >= 5.0):
	print("APROVOU")
else:
	print("REPROVOU")
	