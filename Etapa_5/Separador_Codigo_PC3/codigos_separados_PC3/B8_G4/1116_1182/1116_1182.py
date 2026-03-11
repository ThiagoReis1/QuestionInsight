x = float(input("valor: "))
y = float(input("valor: "))
if(x == 0.0 or y == 0.0):
	print("O ponto (",x,",",y,") estah situado sobre um dos eixos")
elif(x > 0 and y > 0):
	print("O ponto (",x,",",y,") estah no quadrante 1")
elif(x < 0 and y > 0):
	print("O ponto (",x,",",y,") estah no quadrante 2")
elif(x < 0 and y < 0):
	print("O ponto (",x,",",y,") estah no quadrante 3")
elif(x > 0 and y < 0):
	print("O ponto (",x,",",y,") estah no quadrante 4")