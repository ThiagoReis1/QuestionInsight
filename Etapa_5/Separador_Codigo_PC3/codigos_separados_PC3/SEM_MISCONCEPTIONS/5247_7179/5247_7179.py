a  = float(input("salario: "))
b = int(input("codigo: "))


if(b!="ADMINISTRADOR") or (b!="ENGENHEIRO") or (b!="MEDICO") or (b!="OUTROS CARGOS"):
   x = "Dados invalidos"
if((b>0) or (b>200)):
	x = "Dados invalidos" 
else:
   if(b!="ADMINISTRADOR"):
		y = a*0.80
		print("Entradas: R$" a "e codigo" b)
	elif(b!="ENGENHEIRO"):
		y = a*0.65
		print("Entradas: R$" a "e codigo" b)
   elif(b!="MEDICO")
	   y = a*0.60
		print("Entradas: R$" a "e codigo" b)
	elif(b!="OUTROS CARGOS"):
	   y = a*0.55
		print("Entradas: R$" a "e codigo" b)
	