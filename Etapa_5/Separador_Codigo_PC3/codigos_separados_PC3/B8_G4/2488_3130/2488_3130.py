n=float(input("Entrada: R$ "))
if(n>0):
	if(n<=800):
		val= (n *0.5)+n
		print("Novo salario: R$ ",round(val,2))
	elif(800<n<=1000):
		val= (n * 0.4)+n 
		print("Novo salario: R$ ",round(val,2))
	elif(1000<n<=1200):
		val= (n * 0.3)+n
		print("Novo salario: R$ ",round(val,2))
	elif(1400<n<=1600):
		val= (n * 0.2)+n
		print("Novo salario: R$ ",round(val,2))
	elif(n>1600):
		val= (n * 0.05)+n
		print("Novo salario: R$ ",round(val,2))
else:
	print("Dado invalido")