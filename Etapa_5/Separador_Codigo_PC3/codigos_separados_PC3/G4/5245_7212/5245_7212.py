sa= float(input())

print("Entrada: R$",sa)

if(sa==800):
	st= (sa*0.5)+sa
	print("Novo salario: R$",round(st,2))
elif(sa>800 and sa<=1000):
	st= (sa*0.4)+sa
	print("Novo salario: R$",round(st,2))
elif(sa>1000 and sa<=1200):
	st= (sa*0.3)
	print("Novo salario: R$",round(st,2))		
elif(sa>1200 and sa<=1400):
	st= (sa*0.2)+sa
	st=sa+t
	print("Novo salario: R$",round(st,2))
elif(sa>1400 and sa<=1600):
	st= (sa*0.1)+sa
	print("Novo salario: R$",round(st,2))
elif(sa>1600):
	st= (sa*0.05)+sa
	print("Novo salario: R$",round(st,2))
else:
	print("Dado invalido")