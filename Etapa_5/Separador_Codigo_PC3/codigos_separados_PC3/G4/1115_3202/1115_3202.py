x = float(input())
y= int(input())
print("Entradas: R$", x, "e codigo", y)

if not( x > 0) or (y > 104 or y < 101):
	print("Dados invalidos")
elif(y == 101):
	r = (x * 0.80)/100
	total = r + x
	print("Novo salario: R$", round(total,2))
elif (y == 102):
	r = (x * 0.65)/100
	total = r + x
	print("Novo salario: R$", round(total,2))
elif (y == 103):
	r = (x * 0.60)/100
	total = r + x
	print("Novo salario: R$", round(total,2))
else:
	r = (x * 0.55)/100
	total = r + x
	print("Novo salario: R$", round(total,2))