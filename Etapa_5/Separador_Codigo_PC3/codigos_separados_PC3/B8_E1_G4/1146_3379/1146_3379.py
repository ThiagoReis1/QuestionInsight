nome= input("Insira o nome do personagem de Game of Thrones")
if (nome=="Joffrey" or  nome=="Robert" or nome=="Sandor" or nome=="Theon" or nome=="Cersei" or nome=="Jaime" or nome=="Tyrion" or nome=="Jorah" or nome=="Jon"):
	if nome=="Joffrey":
		print("Jack Gleeson")
	elif nome=="Robert":
		print("Mark Addy")
	elif nome=="Sandor":
		print("Rory McCann")
	elif nome=="Theon":
		print("Alfie Allen")
	elif nome=="Cersei":
		print("Lena Headey")
	elif nome=="Jaime":
		print("Nikolaj Coster-Waldau")
	elif nome=="Tyrion":
		print("Peter Dinklage")
	elif nome=="Jorah":
		print("Iain Glen")
	elif nome=="Jon":
		print("Kit Harington")
else:
	print("Entrada",nome,"invalida")