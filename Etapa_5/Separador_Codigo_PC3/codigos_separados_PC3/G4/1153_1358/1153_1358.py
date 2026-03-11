x = float(input("Informe o valor banco do pobresco: "))
y = float(input("Informe o valor banco do bitcoin: "))
tx = float(input("Informe o valor da porcentagem: "))
ty = float(input("Informe o valor da porcentagem: "))
px =(tx/100) + 1
py = (ty/100) + 1
anos = 1
i = 1
while(i > 0):
	x = x +(x * px)
	y = y +(y * py)
	anos = anos + 1
	i = i + 1
print(anos)