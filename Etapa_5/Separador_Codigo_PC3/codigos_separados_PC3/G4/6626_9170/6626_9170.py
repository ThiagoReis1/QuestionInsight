# faça seu código aqui!
n = input("Digite uma palavra: ").upper()

i=0
cont=0
while i<len(n):
	if n[i]=="C":
		cont+=1
	i+=1
print(cont)