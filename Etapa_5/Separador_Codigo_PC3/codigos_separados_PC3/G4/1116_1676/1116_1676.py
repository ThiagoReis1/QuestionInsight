x = float(input("Qual eh o x?: "))
y = float(input("Qual eh o y?: "))

if(x > 0 and y > 0):
	print("O ponto( ", x,",", y," ) estah no quadrante 1")
elif(x < 0 and y > 0):
	print("O ponto( ",x,",", y," ) estah no quadrante 2")
elif(x < 0 and y < 0):
	print("O ponto( ",x,",", y," ) estah no quadrante 3")
elif(x > 0 and y < 0):
	print("O ponto( ",x,",", y," ) estah no quadrante 4")
else:
	print("O ponto( ", x,",", y," ) estah situado sobre um dos eixos")