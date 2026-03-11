e=input("Nome do Estado: ")
c=input("Nome da Cidade: ")

if (e=="Amazonas") and (c=="Manaus"):
	x = "coroado"
	print(x.upper())
elif (e=="Amazonas") and (c=="Parintins"):
	x = "palmares"
	print(x.upper())
elif (e=="Para") and (c=="Belem"):
	x = "cidade velha"
	print(x.upper())
elif (e=="Para") and (c=="Santarem"):
	x = "centro"
	print(x.upper())
else:
	x="bairro nao identificado"
	print(x.upper())