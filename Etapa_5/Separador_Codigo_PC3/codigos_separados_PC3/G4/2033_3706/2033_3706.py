nome= input("")
soma= 0

while(nome.upper()!= "S"):
	if(nome.upper()== "ICOMP"):
		soma = soma + 1
		nome= input("")
	else:
		nome= input("")
if(nome.upper()=="S"):
	print(soma)
