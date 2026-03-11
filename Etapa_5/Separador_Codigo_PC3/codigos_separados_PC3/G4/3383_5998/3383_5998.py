u = input("unidade").upper()
v = float(input("valor"))

if u == "K":
	p = 2.20462*v
	
else:
	p = v/(2.20462)
	
print(round(p,2))