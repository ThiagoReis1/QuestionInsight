tasal = input("Tapioca ou Salgado: ").upper()
qtd_tasal = float(input("Quantidade de tapiocas ou salgados: "))
acai = float(input("Quantidade de acais: "))

salgado = float(qtd_tasal * 5) + (acai * 13)
tapioca = float(qtd_tasal * 3.5) + (acai * 13)

if tasal == "T":
	print(round(tapioca, 2))

if tasal == "S":
	print(round(salgado, 2))