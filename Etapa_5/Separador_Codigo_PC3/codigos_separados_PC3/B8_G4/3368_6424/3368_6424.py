t = str(input()).upper()
q = float(input())
if t == "C":
	temp = q  + 273.15
elif t == 'K':
	temp = q - 273.15
print(round(temp,2))