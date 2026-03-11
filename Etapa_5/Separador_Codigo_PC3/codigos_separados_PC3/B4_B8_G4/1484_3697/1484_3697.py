n = input("nome: ").upper()
c = float(input("carga: "))

if (n!='COMPUTADOR' and n!='FREEZER' and n!='FURADEIRA' and n!='LIQUIDIFICADOR' and n!='MICROONDAS' and n!='NOTEBOOK' and n!='TELEVISOR' and n!='VENTILADOR')or (c<0 or c>1000):  
	print("Entrada invalida")
elif(n=='COMPUTADOR'):
	q=int(c//12)
	print(q)
elif(n=='FREEZER'):
	q=int(c//52)
	print(q)
elif(n=='FURADEIRA'):
	q=int(c//1.7)
	print(q)
elif(n=='LIQUIDIFICADOR'):
	q=int(c//1.8)
	print(q)
elif(n=='MICROONDAS'):
	q=int(c//15)
	print(q)
elif(n=='NOTEBOOK'):
	q=int(c//2.5)
	print(q)
elif(n=='TELEVISOR'):
	q=int(c//15)
	print(q)
elif(n=='VENTILADOR'):
	q=int(c//2.4)
	print(q)
