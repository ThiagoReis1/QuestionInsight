comida = (input("tapioca ou salgado (t/s) "))
qc = int(input("quantos? ")) 
qa = int(input("quantidade de acai? "))

if comida.upper() == "T":
	tapioca = 3.50 * qc
	acai = 13.0 * qa
	conta = tapioca + acai
	print(round(conta, 2))
else:
	salgado = 5.0 * qc
	acai = 13.0 * qa
	conta = salgado + acai
	print(round(conta, 2))