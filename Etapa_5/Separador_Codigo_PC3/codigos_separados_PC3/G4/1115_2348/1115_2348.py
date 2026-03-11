s=float(input("salario atual:"))
c=int(input("codigo:"))
print("Entradas: R$",s,"e codigo",c)
if(c==101):
	x=s+(s*0.8)/100
	print("Novo salario: R$",round(x,2))
elif(c==102):
	x=s+(s*0.65)/100
	print("Novo salario: R$",round(x,2))
elif(c==103):
	x=s+(s*0.6)/100
	print("Novo salario: R$",round(x,2))
elif(c==104):
	x=s+(s*0.55)/100
	print("Novo salario: R$",round(x,2))
else:
	print("Dados invalidos")