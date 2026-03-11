r = input("Insira a regiao aqui: ")
e = input("Insira o estado aqui: ")
if r == "Norte" and e == "Amazonas":
	print("universidade federal do amazonas".upper())
elif r == "Norte" and e == "Roraima":
	print("universidade federal do roraima".upper())
elif r == "Sul" and e == "Parana":
	print("universidade federal do parana".upper())
elif r == "Sul" and e == "Santa Catarina":
	print("universidade federal de santa catarina".upper())
else:
	print("universidade nao identificada".upper())