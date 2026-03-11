r = input("Insira a pais aqui: ")
e = input("Insira o regiao aqui: ")
if r == "Italia" and e == "Roma":
	print("latina".upper())
elif r == "Italia" and e == "Florenca":
	print("siena".upper())
elif r == "Espanha" and e == "Frigiliana":
	print("malaga".upper())
elif r == "Espanha" and e == "Madrid":
	print("madrid".upper())
else:
	print("provincia nao identificada".upper())