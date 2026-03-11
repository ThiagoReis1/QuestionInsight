from numpy import *

C = array(eval(input("insira 3 notas")))
PP = array([2, 1, 5])

media = 0
num = 0

while media < size(C):
	num += C[media] * PP[media]
	media += 1
	
media = num / sum(PP)
print(round(media, 2))