s = float(input("salaio: "))
c = int(input("codigo 101/102/103/104: "))

if((s >= 0) and (c == 101 or c == 102 or c == 103 or c == 104)):
	if(c == 101):
		t = (s + s*0.80/100)
		print("Novo salario: R$ ",round(t,2))
		
	elif(c == 102):
		t = (s + s*0.65/100)
		print("Novo salario: R$" , round(t,2))
		
	elif(c == 103):
		t = (s + (s*0.60)/100)
		print("Novo salario: R$ " ,round(t,2))
		
	elif(c == 104):
		t = (s + s*0.55/100)
		print("Novo salario: R$ " , round(t,2) )
		
else:
	print("Dados invalidos")