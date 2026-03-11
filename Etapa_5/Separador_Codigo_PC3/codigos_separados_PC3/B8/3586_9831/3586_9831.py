from numpy import *

i= 0
pontuacao= 0

anel= array(eval(input("Entre com a sua pontuacao: ")))

while i < len (anel):
	if anel[i] == 1:
		pontuacao += 100
		
	elif anel[i] == 2: 
		pontuacao += 60
	
	elif anel[i] == 3: 
		pontuacao += 20
	
	elif anel[i] == 4:
		pontuacao += 0
	i= i + 1
	
print(pontuacao)