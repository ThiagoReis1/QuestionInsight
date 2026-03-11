
#como salarios
s=float(input("salario:"))
c=int(input("codigo:"))
print("Entradas: R$",s, "e codigo",c,)
#administrador
if (c==101) and (c>0):
	a=s+((s*80)/100)
	print("Novo salario: R$",a,)
elif c==102 and c>0 :
	e=s+((s*65)/100)
	print("Novo salario: R$",e,)
elif (c==103) and c>0 :
	m=s+((s*60)/100)
	print("Novo salario: R$",m,)
	
elif(c==104)and(c>0):
	o=s+((s*55)/100)
	print("Novo salario: R$",o,)
else:
	print("Dados invalidos")
	
	
	
	
	

	
