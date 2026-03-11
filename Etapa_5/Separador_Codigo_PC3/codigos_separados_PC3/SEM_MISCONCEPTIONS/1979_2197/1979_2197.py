resultado = input("Digite resultado da seleção: ")
numero_de_resultados = input("Número de vezes em que foi campeão: ")

if resultado == "Campeao" and numero_de_resultados == "05-vezes":
	print("brasil".upper())
elif resultado == "Campeao" and numero_de_resultados == "04-vezes":
	print("italia".upper())
elif resultado == "Vice-Campeao" and numero_de_resultados == "04-vezes":
	print("alemanha".upper())
elif resultado == "Vice-Campeao" and numero_de_resultados == "03-vezes":
	print("argentina".upper())
else:
	print("selecao nao identificada".upper())