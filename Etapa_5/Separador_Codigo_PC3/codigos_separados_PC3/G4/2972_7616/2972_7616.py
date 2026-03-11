s = int(input("Posicao final? "))
v = int(input("Velocidade do Objeto? "))
t = int(input("Tempo do Deslocamento? "))

formula = s + (v*t)

if formula <=1000:
	print(formula)
	print("Nao")
else:
	print(formula)
	print("Sim")