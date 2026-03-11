from numpy import*
e=(input("").upper())
i=0
soma=0
while i<len(e):
	if e[i]=="A" or e[i]=="E" or e[i]=="I" or e[i]=="O" or e[i]=="U":
		soma=soma+35.15
	else:
		soma=soma+42.17
	i=i+1
print(round(soma,2))
	