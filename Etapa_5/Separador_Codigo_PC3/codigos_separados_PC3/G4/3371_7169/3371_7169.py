c = input("digite").upper()
v = float(input("valor da medida"))
if c=="K":
	a = 1000*v//1.60934/1000
else:
	a = v*1.609341
	
print(round(a, 2))