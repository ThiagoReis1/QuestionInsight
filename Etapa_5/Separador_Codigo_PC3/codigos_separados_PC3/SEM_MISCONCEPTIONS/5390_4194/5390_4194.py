from numpy import*
R = input("Nome da etiqueta: ")
i = 0
custo = 0

while(i < len( R )):
	if( R[i] == "A" or R[i]=="E" or R[i]=="I" or R[i]=="O" or R[i]=="U"): 
		custo = custo + 0.19
	else:
		custo = custo + 0.23
	i = i + 1
	
print( round(custo, 2))