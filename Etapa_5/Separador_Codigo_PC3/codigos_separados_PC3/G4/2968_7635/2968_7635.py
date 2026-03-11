a = input("L/S?")
e = "L"
if(a == e):
	b = float(input("lanches:"))
	ms = (b * 5)
else:
	d = float(input("salgados:"))
	ms = (d * 3.5)
c = float(input("refrigerantes:"))
print(ms + (c * 4))