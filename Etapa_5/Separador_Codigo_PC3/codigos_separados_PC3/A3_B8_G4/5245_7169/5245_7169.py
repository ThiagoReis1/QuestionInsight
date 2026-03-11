a = float(input("salario atual de um funcionario"))
print("Entrada: R$", a)
if(a <= 1600) or (a <= 1600):
	l = (a*0.50+a)
	print(round(l,2))	
	if(a>=800) or (a<=1000):
		b = (a*0.40+a)
		print(round(a*0.40+a, 2))
	elif(a >= 1000) or (a <= 1200):
		h = (a*0.30+a)
		print(round(h, 2))	
	elif(a >= 1200) or (a <= 1400):
		p = (a*0.20+a)
		print(round(p, 2))		
	elif(a>=1400) or (a>=1600):
		u = (a*0.10+a)
		print(round(u, 2))
if(a >= 800 and a > 0):
	y = (a*0.50+a)
	print(round(y, 2))
else:
	print("Dado invalido")