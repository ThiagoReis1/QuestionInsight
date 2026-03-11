#custo
cod=input("Digite o codigo:").upper()

i=0
custo=0

while(i<len(cod)):
	if (cod[i]=="A") or (cod[i]=="E") or (cod[i]=="I") or (cod[i]=="O") or (cod[i]=="U"):
		custo= custo + 35.15
	else:
		custo= custo + 42.17
	i=i+1
print(round((custo),2))