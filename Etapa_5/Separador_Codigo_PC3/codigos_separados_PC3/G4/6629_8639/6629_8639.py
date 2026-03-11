# faça seu código aqui!
s= (input("Digite a palavra: ")). upper()
i=0
cont=0
while i<len(s):
	if s[i]=="P":
		print(i)
		cont+=1
	i+=1
if  cont == 0:
	print("nao achei")
		
		
	
