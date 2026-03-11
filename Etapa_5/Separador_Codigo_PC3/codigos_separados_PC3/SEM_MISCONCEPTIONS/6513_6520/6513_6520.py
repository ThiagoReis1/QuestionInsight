# faça seu código aqui!
m=float(input("manha energetica: "))
a=20

if m >= 4:
	desconto=m*20*(15/100)
	vtotal=m*a-desconto
	
else:
	vtotal=m*a
print(round(vtotal,2))
	