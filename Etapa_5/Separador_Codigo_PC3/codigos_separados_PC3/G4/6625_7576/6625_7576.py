# faça seu código aqui!

a = input("insira: ").upper()
i = 0
cont = 0
while(i < len(a)):
	if(a[i] == "B"):
		cont += 1
	i += 1 
	
print(cont)	