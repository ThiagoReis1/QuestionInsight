valor = float(input("Digite um valor "))
menos = valor*1.20
multa = 25 + valor*1.40
if(valor <= 100):
	print(menos)
else:
	print(round(multa ,2))

