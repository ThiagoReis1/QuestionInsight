b=input().upper()
i=0
soma=0
while i< len(b):
	if b[i]=="H":
		soma=soma+5.40
	elif b[i]=="C":
		soma=soma+8.95
	elif b[i]=="L":
		soma=soma+4.50
	i=i+1
print(round(soma,2))
		