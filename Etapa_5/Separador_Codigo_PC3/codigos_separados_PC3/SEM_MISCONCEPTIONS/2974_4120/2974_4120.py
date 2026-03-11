a = float(input("Digite o peso em gramas de acai no copo: "))
s = float(input("Digite a quantidade de salgados comprados: "))
p = float(input("Digite o valor pago em dinheiro: "))

acaiKG = 24.0
salgadoUni = 3.0

precoacai = (a/1000)*acaiKG
precosalgado = (s*salgadoUni)

print(round(precoacai + precosalgado, 2))

if(p <= precoacai + precosalgado):
	print("Nao")
else:
	print("Sim")