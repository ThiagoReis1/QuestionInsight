s = float(input("salario atual: "))

if(0<s)and(s<=800):
	a = s * (50/100)
	b = s + a
	print("Novo salario: R$ ",round(b,2))
elif(1000>=s)and(s>800):
	a = s *(40/100)
	b=s+a
	print("Novo salario: R$ ",round(b,2))
elif(1200>=s)and(s>1000):
	a=s*(30/100)
	b=s+a
	print("Novo salario: R$ ",round(b,2))
elif(1400>=s)and(s>1200):
	a=s*(20/100)
	b=s+a
	print("Novo salario: R$ ",round(b,2))
elif(1600>=s)and(s>1400):
	a=s*(10/100)
	b=s+a
	print("Novo salario: R$ ",round(b,2))
elif(s>1600):
	a=s*(5/100)
	b=s+a
	print("Novo salario: R$ ",round(b,2))
else:
	print("Dado invalido")
