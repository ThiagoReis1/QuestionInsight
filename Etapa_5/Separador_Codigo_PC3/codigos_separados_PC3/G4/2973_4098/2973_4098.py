from math import *

s0 = int(input("posicao inicial do objeto: "))
v = int(input("velocidade de deslocamento: "))
t = int(input("tempo de deslocamento: "))	  

S = s0 + (v*t)
			  
if (v <= 100) :
	print(S)
	mensagem = " OK"
	print(mensagem)
else:
	print(S)
	mensagem = " ACIMA"
	print(mensagem)
