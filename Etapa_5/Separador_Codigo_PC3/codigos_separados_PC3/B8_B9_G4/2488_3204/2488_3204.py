s = float(input())

if(s>0):
	if(s<= 800):
		n= s+ s*0.5
		print("Entrada: R$", s)
		print("Novo salario: R$", round(n , 2))
	elif(s>800 and s<=1000):
		n = s+ s *0.4
		print("Entrada: R$", s)
		print("Novo salario: R$", round(n, 2))
	elif(s>1000 and s <=1200):
		n = s+ s*0.3
		print("Entrada: R$", s)
		print("Novo salario: R$", round(n, 2))
	elif(s>1200 and s<=1400):
		n = s+s*0.2
		print("Entrada: R$", s)
		print("Novo salario: R$", round(n, 2))
	elif(s>1400 and s <=1600):
		n = s+s*0.1
		print("Entrada: R$", s)
		print("Novo salario: R$", round(n, 2))
	elif(s>1600):
		n = s+s*0.05
		print("Entrada: R$", s)
		print("Novo salario: R$", round(n, 2))		
		
else:
	print("Entrada: R$", s)
	print("Dado invalido")