v= input("").upper()
i=0
soma=0

while(len(v)>i):
	if(v[i]=="A" or v[i]=="E" or v[i]=="I" or v[i]=="O" or v[i]=="U"):
		soma=soma+0.15
	else:
		soma=soma+0.17
	i=i+1
print(round(soma,2))