v = input("Digite um nome: ")

if v[4] == "c" or v[4] == "C":
	v = v.upper()
else:
	v = "nome invalido"
	
print(v)