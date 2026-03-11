from numpy import *
s = input('escreva uma string qualquer: ').upper()
i = 0 
aparicoes = 0

while i < len(s):
	if s[i] == 'C':
		aparicoes+=1
	i+= 1
print (aparicoes)