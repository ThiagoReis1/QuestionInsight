s=float(input("Salario atual"))

print("Entrada: R$",s)

if(s>0):
	if(s<=800):
		r=(s*0.5)+s
	elif(s>800 and s<=1000):
		r=(s*0.4)+s
	elif(s>1000 and s<=1200):
		r=(s*0.3)+s
	elif(s>1200 and s<=1400):
		r=(s*0.2)+s
	elif(s>1400 and s<1600):
		r=(s*0.1)+s
	else:
		r=(0.05*s)+s
	
	print("Novo salario: R$ ",round(r,2))	
else:
	print("Dado invalido")