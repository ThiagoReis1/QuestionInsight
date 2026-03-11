a=float(input("salario atual:"))		
print("Entrada: R$",a)
if(a<=800 and a>0):
	print("Novo salario: R$",round((a+(a*0.5)),2))
elif(a>800 and a<=1000):
	print("Novo salario: R$",round((a+(a*0.4)),2))
elif(a>1000 and a<=1200):
	print("Novo salario: R$",round((a+(a*0.3)),2))
elif(a>1200 and a<=1400):
	print("Novo salario: R$",round((a+(a*0.2)),2))
elif(a>1400 and a<=1600):
	print("Novo salario: R$",round((a+(a*0.1)),2))
elif(a>1600):
	print("Novo salario: R$",round((a+(a*0.05)),2))
else:
	print("Dado invalido")
	
