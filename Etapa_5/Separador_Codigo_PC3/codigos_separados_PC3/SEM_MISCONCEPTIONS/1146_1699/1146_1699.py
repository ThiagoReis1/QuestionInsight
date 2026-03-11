#--------------------------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# ANA REBECA CAVALCANTE EVANGELISTA
# MATRICULA: 21456290
# DATA: 14/07/2016
#--------------------------------------------------------------

nome = input("Digite o nome do personagem de GoT: ")

if (nome == "Joffrey" or nome == "joffrey"):
	result = "Jack Gleeson"
elif (nome == "Robert" or nome == "robert"):
	result = "Mark Addy"
elif (nome == "Sandor" or nome == "sandor"):
	result = "Rory McCann"
elif (nome == "Theon" or nome == "theon"):
	result = "Alfie Allen"
elif (nome == "Cersei" or nome == "cersei"):
	result = "Lena Headey"
elif (nome == "Jaime" or nome == "jaime"):
	result = "Nikolaj Coster-Waldau"
elif (nome == "Tyrion" or nome == "tyrion"):
	result = "Peter Dinklage"
elif (nome == "Jorah" or nome == "jorah"):
	result = "Iain Glen"
elif (nome == "Jon" or nome == "jon"):
	result = "Kit Harington"
else:
	result = "invalido"
if (result != "invalido"):
	print (result)
else:
	print ("Entrada", nome, "invalida")