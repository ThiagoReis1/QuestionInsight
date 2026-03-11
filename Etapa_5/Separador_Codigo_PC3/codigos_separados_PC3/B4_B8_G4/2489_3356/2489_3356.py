from math import*
cd = input()
i = int(input())

if(i>0and i<150):
	if(cd=="Porto Velho") and (i<=2):
		v = 0
		print("Entradas:",cd,",",i)
		print("Passagem: R$",round(v,2))

	elif(cd=="Porto Velho")and (3 <=i) and (i<=12):
		v =  500-(500* 0.5)
		print("Entradas:",cd,",",i)
		print("Passagem: R$",round(v,2))
	
	elif(cd=="Porto Velho")and (i>=65):
		v = 500-(500* 0.3)
		print("Entradas:",cd,",",i)
		print("Passagem: R$",round(v,2))
	
	
	elif(cd=="Santarem")and (i<=2):
		v = 0
		print("Entradas:",cd,",",i)
		print("Passagem: R$",v)
	elif(cd=="Santarem")and (3 <=i) and (i<=12):
		v =  370-(370* 0.5)
		print("Entradas:",cd,",",i)
		print("Passagem: R$",round(v,2))
	elif(cd=="Santarem")and (i>=65):
		v = 370-(370* 0.3)
		print("Entradas:",cd,",",i)
		print("Passagem: R$",round(v,2))
	
	
	elif(cd=="Belem")and (i<=2):
		v = 0
		print("Entradas:",cd,",",i)
		print("Passagem: R$",v)
	elif(cd=="Belem")and (3 <=i) and (i<=12):
		v =  600-(600* 0.5)
		print("Entradas:",cd,",",i)
		print("Passagem: R$",round(v,2))
	elif(cd=="Belem")and (i>=65):
		v = 600 -(600* 0.3)
		print("Entradas:",cd,",",i)
		print("Passagem: R$",round(v,2))
		
		
	elif(cd=="Tefe")and (i<=2):
		v = 0
		print("Entradas:",cd,",",i)
		print("Passagem: R$",v)
	elif(cd=="Tefe")and (3 <=i) and (i<=12):
		v = 360-( 360* 0.5)
		print("Entradas:",cd,",",i)
		print("Passagem: R$",round(v,2))
	elif(cd=="Tefe")and (i>=65):
		v =360-(360* 0.3)
		print("Entradas:",cd,",",i)
		print("Passagem: R$",round(v,2))
		
	
	elif(cd=="Tabatinga")and (i<=2):
		v = 0
		print("Entradas:",cd,",",i)
		print("Passagem: R$",v)
	elif(cd=="Tabatinga")and (3 >=i>=12):
		v =  550-(550* 0.5)
		print("Entradas:",cd,",",i)
		print("Passagem: R$",round(v,2))
	elif(cd=="Tabatinga")and (i>=65):
		v = 550-(550* 0.3)
		print("Entradas:",cd,",",i)
		print("Passagem: R$",round(v,2))
else:
	print("Entradas:",cd,",",i)
	print("entradas invalidas")