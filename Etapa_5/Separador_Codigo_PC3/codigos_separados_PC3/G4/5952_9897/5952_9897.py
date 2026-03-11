tipo = input('digite (T) para tapioca e (S) para salgado: ')
qntd_ts = int(input('quantidade de tapiocas ou salgados: '))
qntd_acai = int(input('quantidade de acais: '))

t = 3.50
s = 5.00
a = 13.00

if tipo == "T":
	v = (t * qntd_ts) + (a * qntd_acai)
	print(round(v, 2))
else:
	v = (s * qntd_ts) + (a * qntd_acai)
	print(round(v, 2))