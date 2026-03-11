uni = input("qual a medida de unidade(B/W): ")
val = float(input("valor da medida: "))
n = 3.41214
if (uni == "B"):
	cal = ((val)/(n))
else:
	cal = ((val) * (n))
print(round(cal, 2))