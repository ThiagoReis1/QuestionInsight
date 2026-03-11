#Universidade Federal do Amazonas
#prova: questão 1
#aluna: Ingrid de Lira Lima

v=float(input("qual a velocidade do trem?"))
t= float(input("tempo de viajem:"))
print("Entradas:", v, "km/h e" ,t, "h")

km= v*t
if(km==250):
	print("Proxima parada:Hogsmead")	
elif(km == 650):
	print("Proxima parada:Gondor")
elif(km==800):
  	print("Proxima parada:Fangorn")
elif(km==1000):
 	print("Proxima parada:Edoras")
elif(km==1200):
	print("Proxima parada:Doriath")
elif(km==1300):
	print("Proxima parada:Castamare")
elif(km==1400):
	print("Proxima parada:Bravos")
elif(km>=1500):
	print("Proxima parada:Avalon")
else:
	print("Dados invalidos")
	
	
	
	
	
