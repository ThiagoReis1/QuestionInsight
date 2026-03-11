tapioca_salgado = input("T para tapioca ou S para salgado: ")
quantidade_ts = int(input("Quantidade de tapiocas ou salgados: "))
quantidade_acai = int(input("Quantidade de acai: "))

if tapioca_salgado.upper() == "T":
	total = quantidade_ts * 4.50 + quantidade_acai * 12.00
else:
	total = quantidade_ts * 5.00 + quantidade_acai * 12.00
print(round(total,2))