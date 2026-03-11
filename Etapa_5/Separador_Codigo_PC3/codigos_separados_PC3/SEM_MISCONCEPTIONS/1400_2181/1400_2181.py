x = input("Digite o tipo de ataque: ")
y = int(input("Digite o numero de rodadas: "))
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
N = valor1 + valor2

if	(x.lower() == 'constricao'):
	constricao = (N + 1) * y
	print(constricao)
if	(x.lower() == 'polen'):
	polen = valor1 * valor2
	print(polen)