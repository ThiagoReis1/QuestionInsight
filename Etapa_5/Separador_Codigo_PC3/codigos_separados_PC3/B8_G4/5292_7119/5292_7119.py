r=input()
cont=0
soma=0
while(r.upper()!="S"):
	if(r.upper()=="VERMELHA"):
		cont=cont+1
	elif(r.upper()=="PRETA"):
		cont=cont+1
		soma=soma+1
	r=input()

total = 100*soma/cont

print(cont)
print(round(total,2))