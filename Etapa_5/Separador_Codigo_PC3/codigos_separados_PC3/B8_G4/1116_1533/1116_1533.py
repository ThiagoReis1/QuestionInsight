x = float(input("digite o valor de x: "))
y = float(input("digite o valor de y: "))
if (x >0) and (y > 0):
	print("O ponto","(" , x ,",", y,")" ,  "estah no quadrante 1")
elif (x <0) and (y > 0):
	print("O ponto","(" , x ,",", y,")" ,  "estah no quadrante 2")
elif (x <0) and (y < 0):
	print("O ponto","(" , x ,",", y,")" ,  "estah no quadrante 3")
elif (x>0) and (y<0):
	print("O ponto","(" , x ,",", y,")" ,  "estah no quadrante 4")
elif (x == 0) and (y == 0):
	print("O ponto","(" , x ,",", y,")" ,  "estah situado sobre um dos eixos")