x = float(input("Digite x: "))
y = float(input("Digite y: "))
if (x > 0 and y > 0):
	ponto = "no quadrante 1"
elif(x < 0 and y > 0):
	ponto = "no quadrante 2"
elif(x < 0 and y < 0):
	ponto = "no quadrante 3"
elif(x > 0 and y < 0):
	ponto = "no quadrante 4"
elif(x == 0 or y == 0):
	ponto = "situado sobre um dos eixos"
print("O ponto (", x, ",", y,") estah", ponto)