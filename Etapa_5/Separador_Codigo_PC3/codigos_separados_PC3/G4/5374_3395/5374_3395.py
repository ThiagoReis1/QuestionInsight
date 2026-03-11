from numpy import*

em=(input("").upper())
i=0
soma=0
while i < len(em):
	if em[i]=="A" or em[i]=="E" or em[i]=="I" or em[i]=="O" or em[i]=="U":
		soma=soma+0.15
	else:
		soma=soma+0.17
	i=i+1
print(round(soma, 2))

