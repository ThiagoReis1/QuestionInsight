x = float(input("Qual o valor do salario "))
if(x<=800 and x>0):
	y=x+(x*0.5)
	print("Entrada: R$",x)
	print("Novo salario: R$",round(y,2))
elif(x>800 and x<=1000):
	y=x+(x*0.4)
	print("Entrada: R$",x)
	print("Novo salario: R$",round(y,2))
elif(x>1000 and x<=1200):
	y=x+(x*0.3)
	print("Entrada: R$",x)
	print("Novo salario: R$",round(y,2))
elif(x>1200 and x<=1400):
	y=x+(x*0.2)
	print("Entrada: R$",x)
	print("Novo salario: R$",round(y,2))
elif(x>1400 and x<=1600):
	y=x+(x*0.1)
	print("Entrada: R$",x)
	print("Novo salario: R$",round(y,2))
elif(x>1600):
	y=x+(x*0.1)
	print("Entrada: R$",)

print("Entrada: R$ ", x)
print("Dado invalido")