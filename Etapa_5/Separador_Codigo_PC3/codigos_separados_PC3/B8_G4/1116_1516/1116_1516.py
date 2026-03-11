x = float(input("Digite a coordenada1:"))
y = float(input("Digite a coordenada2:"))

if((x > 0) and (y > 0)):
	print("o ponto", "(",x, "," , y,")estah no quadrante 1")
elif((x < 0) and (y > 0)):
	print("o ponto", "(",x, "," , y,")estah no quadrante 2")
elif((x < 0) and (y < 0)):
	print("o ponto","(", x, "," , y,")estah no quadrante 3")
elif((x > 0) and (y > 0)):
	print("o ponto","(", x, "," , y,") estah no quadrante 4")