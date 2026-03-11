a = input("nome do equipamento:")
b = int(input("quantidade a ser transportada:"))

if(a=="COMPUTADOR")and((b>0)and(b<1000)):
	print (round((b*12),2))
elif(a=="FREEZER")and((b>0)and(b<1000)):
	print (round((b*52),2))
elif(a=="FURADEIRA")and((b>0)and(b<1000)):
	print (round((b*1.7),2))
elif(a=="LIQUIDIFICADOR")and((b>0)and(b<1000)):
	print (round((b*1.8),2))
elif(a=="MICROONDAS")and((b>0)and(b<1000)):
	print (round((b*15),2))
elif(a=="NOTEBOOK")and((b>0)and(b<1000)):
	print (round((b*2.5),2))
elif(a=="TELEVISOR")and((b>0)and(b<1000)):
	print (round((b*15),2))
elif(a=="VENTILADOR")and((b>0)and(b<1000)):
	print (round((b*2.4),2))
else:
	print("Entrada invalida")