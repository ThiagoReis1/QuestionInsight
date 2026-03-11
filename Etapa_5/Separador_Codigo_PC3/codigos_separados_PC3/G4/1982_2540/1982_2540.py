P = input("nome do pais:")
C = input("nome da cidade:")

if((P == "Italia")and(C == "Roma")):
	print("latina".upper())
elif((P == "Italia")and(C == "Florença")):
	print("Siena".upper())
elif((P == "Espanha")and(C == "Frigiliana")):
	print("Malaga".upper())
elif((P == "Espanha")and(C == "Madrid")):
	print("Madrid".upper())
else:
	print("provincia nao identificada".upper())