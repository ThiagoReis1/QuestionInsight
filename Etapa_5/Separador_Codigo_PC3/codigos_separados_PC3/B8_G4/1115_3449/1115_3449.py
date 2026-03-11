sla=float(input("salario: "))
cod=int(input("codigo: "))

print("Entradas: R$",sla, "e", "codigo",cod)

if	(sla>0) and (cod==101) or (cod==102) or (cod==103) or (cod==104):
	if	(cod==101):
		ns= (sla*0.80)/100
		nss= ns+sla
		print("Novo salario: R$",round(nss,2))
	elif	(cod==102):
		ns= (sla*0.65)/100
		nss= ns+sla
		print("Novo salario: R$",round(nss,2))
	elif	(cod==103):
		ns= (sla*0.60)/100
		nss= ns+sla
		print("Novo salario: R$",round(nss,2))
	elif	(cod==104):
		ns= (sla*0.55)/100
		nss= ns+sla	
		print("Novo salario: R$",round(nss,2))
		
		
else:
	print ("Dados invalidos")