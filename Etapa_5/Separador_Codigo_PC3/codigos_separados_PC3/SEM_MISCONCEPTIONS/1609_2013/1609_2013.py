#biblioteca
from numpy import*
#tempo de corrida

palavra= array (eval(input("palavras:")))
dicionario = array (eval(input("palavras:")))
i=0
while i<size(palavra):
	if palavra[i] != dicionario.replace('R','L'):
		i=i+1
else:
	print(i-1)
	


