rotacao = float(input("digite o valor da rotacao (RPM): "))

frequencia = 50

print(rotacao)
while frequencia < rotacao:
	perda = rotacao*0.25
	rotacao = rotacao - perda
	if rotacao > 50:
		print(round(rotacao, 2))
