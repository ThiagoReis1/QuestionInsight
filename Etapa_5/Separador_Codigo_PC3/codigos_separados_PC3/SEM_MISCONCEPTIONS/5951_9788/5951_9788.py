tapioca = 4.50
salgado = 5.00
acai = 12.00

TS = input("coloque T ou S:")


if (TS == "T"):
	quant_tap = int(input('quantidade de tapioca:'))
	quant_acai = int(input('quantidade de acai:'))
	total = (quant_tap * tapioca) + (quant_acai * acai)
	print(round(total, 1))

if(TS == 'S'):
	quant_salg = int(input('quantidade de salgdo:'))
	quant_acai = int(input('quantidade de acai:'))
	total = (quant_salg * salgado) + (quant_acai * acai)
	print(round(total, 1))