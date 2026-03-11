# leia x
x = float(input("Informe valor de x: "))

# condicao se x menor ou igual a -1 ou f(x) maior ou igual a 1
if (x <= -1) or (x >= 1):
	# exibe valor arredondado em duas casas
	print(round(x,2))
# condicao se x maior que menos 1 e x menor que zero ou x maior que zero e x menor que um
elif (x > -1 and x < 0) or (x > 0 and x < 1):
	# exibe resultado da condicao
	print(round(1))
# condicao se x igual a zero
elif x == 0:
	# exibe resultado da condicao
	print(round(2))