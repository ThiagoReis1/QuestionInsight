item = input("T para tapioca ou S para salgado: ").upper()
qntd_ts = int(input("quantidade de tapiocas ou salgados: "))
qntd_a = int(input("quantidade de acais: "))

if item == "T":
	total = (qntd_ts * 5.5)+(qntd_a * 10)
	print(round(total, 2))
if item == "S":
	total = (qntd_ts * 4)+(qntd_a * 10)
	print(round(total, 2))