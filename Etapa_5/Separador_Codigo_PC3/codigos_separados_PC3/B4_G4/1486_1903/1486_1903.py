n = input("digite o nome: ").upper()
q = int(input("digite a quantidade: "))

if((q<0) and (q>10000)):
	print("Entrada invalida")
	
elif((n == "ARROZ") and (q>=0) and (q<=10000)):
	t = q/500
	print(int(t))

elif((n=="CENOURA") and (q>=0) and (q<=10000)):
	t = q/100
	print(int(t))
	
elif((n=="KAMPYO") and (q>=0) and (q<=10000)):
	t = q/20
	print(int(t))
	
elif((n=="NORI") and (q>=0) and (q<=10000)):
	t = q/50
	print(int(t))
	
elif((n=="OMELETE") and (q>=0) and (q<=10000)):
	t = q/200
	print(int(t))
	
elif((n=="PEPINO") and (q>=0) and (q<=10000)):
	t = q/150
	print(int(t))
	
elif((n=="SALMAO") and (q>=0) and (q<=10000)):
	t = q/300
	print(int(t))
	
elif((n=="SHITAKE") and (q>=0) and (q<=10000)):
	t = q/150
	print(int(t))

else:
	print("Entrada invalida")