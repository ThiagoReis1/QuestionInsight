u = str(input("unidade de maedida:").upper())
v = float(input("valor da encomenda:"))

if(u =="W"):
	m = 3.41214*v
else:
	m = v/3.41214
print(round(m,2))