from math import *
populacao = int(input())
taxa = float(input())
retirada = int(input())

anos = 1

while(populacao > 0):
	anos = anos + 1
	populacao = populacao + int(populacao * taxa)
	populacao = populacao - retirada
	
print(anos)