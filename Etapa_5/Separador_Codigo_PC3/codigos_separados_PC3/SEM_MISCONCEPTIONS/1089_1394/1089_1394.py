# Hadassa Duperron Mat.21601100
# Introd. A Prog. de Computadores
# Avaliacao Parcial 2   30 / 06 / 2016

a = float(input("Digite o valor da compra a: "))
b = float(input("Digite o valor da compra b: "))
c = float(input("Digite o valor da compra c: "))
lim_c = float(input("valor do limite: "))
valor_total = (a + b + c)
print(round(valor_total, 2))

if (valor_total <= lim_c) :
	print("Sim")
else:
	print("Nao")
print
	