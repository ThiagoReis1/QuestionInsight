from numpy import*
p = input("Digite uma palavra: ").upper()
i = 0
custo = 0
while i<len(p):
	if p[i]=="A" or p[i]=="E" or p[i]=="I" or p[i]== "O" or p[i]== "U":
		custo= custo + 45.15
	else:
		custo = custo + 50.17
	i = i+1

print(round(custo,2))