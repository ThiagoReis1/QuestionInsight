from numpy import *

vetor = array (eval(input("")))
palavra =input("")
i=0
contador = 0 
while( vetor[i].upper() != palavra.upper().replace("R","L")):
	
	i = i + 1

if( contador == 0):
	print("NAO ENCONTRADA")
else:
	print(i)
	
	
	
