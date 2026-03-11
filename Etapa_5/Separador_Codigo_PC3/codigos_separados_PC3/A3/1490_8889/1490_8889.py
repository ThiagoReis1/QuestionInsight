v = float(input(''))

if v >= 0.0 and v <= 10.0:
	valor = v * 3.0 + 15.0
if v > 10.0 and v <= 15.0:
	valor= v * 3.50 + 20.0
if v > 15.0 and v <= 20.0:
	valor = v * 4.0 + 25.0
if v > 20.0:
	valor = v * 4.50 + 30.0

print(round(valor,2))