from numpy import*

S=input("Quantidade de vitorias: ").upper()
cont=0

while S != 'X':
	if S == 'A':
		cont=cont+1
	S=input("Quantidade de vitrias: ").upper()
	
print(cont)
	
