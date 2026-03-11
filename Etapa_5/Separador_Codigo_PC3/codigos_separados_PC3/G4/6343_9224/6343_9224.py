n = input("Digite um nome:")

if len(n) >= 2 and n[1].lower() == "a":
	print(n.upper())
else:
   print("nome invalido")