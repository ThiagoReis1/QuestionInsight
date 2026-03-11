x=float(input("Salario atual:"))
y=input("Codigo do Cargo:")
print("Entradas: R$",x,"e codigo", y)

if(x<=0):
	print("Dados invalidos")
	
elif((y!="101")and(y!="102")and(y!="103") and (y!="104")):
	print("Dados invalidos")
	
elif(y=="101"):
	print("Novo salario: R$ ", round((x+x*0.008),2))
	
elif(y=="102"):
	print("Novo salario: R$ ", round((x+x*0.0065),2))
	
elif(y=="103"):
	
	print("Novo salario: R$ ", round((x+x*0.0060),2))
elif(y=="104"):
	print("Novo salario: R$ ", round((x+x*0.0055),2))
	
