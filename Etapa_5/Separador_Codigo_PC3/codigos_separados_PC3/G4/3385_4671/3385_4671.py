x=str(input("Digite A para acres ou H para hectares: "))
x=x.upper()
y=float(input("Valor da medida: "))

if(x=='H'):
	m=2.47105*y
else: 
	m=y/2.47105
print(round(m,2))