nome = input("")

i = 0

while(nome.upper() != "S"):
	if(nome == "ICOMP"):
		i = i + 1
	nome = input("")

print(i)