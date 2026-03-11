s=float(input("digite o salario do funcionário:"))
print("Entrada: R$",s)
if (s<0):
	print("Dado invalido")
elif(s<=800):
	s=s+s*0.5
	print("Novo salario: R$",round(s,2))
elif(s>800 and s<=1000):
	s=s+s*0.4
	print("Novo salario: R$",round(s,2))
elif(s>1000 and s<=1200):
	s=s+s*0.3
	print("Novo salario: R$",round(s,2))
elif(s>1200 and s<=1400):
	s= s+s*0.2
	print("Novo salario: R$",round(s,2))
elif(s>1400 and s<=1600):
	s= s + s*0.1
	print("Novo salario: R$",round(s,2))
else:
	s= s + s*0.05
	print("Novo salario: R$",round(s,2))
	