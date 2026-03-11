c = float(input("graus em celsus: "))
k = float(input("graus em kelvin: "))
co = 273,15
celsus = float(k - co)
kelvin = float(c + co)
if (c > 0) and (c < 0) and (c == 0):
	print(round(celsus, 2))
elif (k > 0) and (k < 0) and (c == 0):
	print(round(kelvin, 2))
