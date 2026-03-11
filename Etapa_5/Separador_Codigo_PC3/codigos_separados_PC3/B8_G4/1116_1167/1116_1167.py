x = float(input("Coordenada X: "))
y = float(input("Coordenada Y: "))
if(x > 0):
	if(y > 0):
		print("O ponto (", x, ",", y, ") estah no quadrante 1")
	elif(y < 0):
		print("O ponto (", x, ",", y, ") estah no quadrante 4")
elif(x < 0):
	if(y > 0):
		print("O ponto (", x, ",", y, ") estah no quadrante 2")
	elif(y < 0):
		print("O ponto (", x, ",", y, ") estah no quadrante 3")
else:
	print("O ponto (", x, ",", y, ") estah situado sobre um dos eixos")