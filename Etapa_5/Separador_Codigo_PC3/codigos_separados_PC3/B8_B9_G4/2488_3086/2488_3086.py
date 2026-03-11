s = float(input("digite o valor do salario: "))
print("Entrada: R$", s)
if(s<0):
	print("Dado invalido")
elif(s<=800):
	print("Novo salario: R$", round(s*(50./100)+s, 2))
elif(s>800 and s<=1000):
	print("Novo salario: R$", round(s*(40./100)+s, 2))
elif(s>1000 and s<=1200):
	print("Novo salario: R$", round(s*(30./100)+s, 2))
elif(s>1200 and s<=1400):
	print("Novo salario: R$", round(s*(20./100)+s, 2))
elif(s>1400 and s<=1600):
	print("Novo salario: R$", round(s*(10./100)+s, 2))
elif(s>1600):
	print("Novo salario: R$", round(s*(5./100)+s, 2))

	


	

			
			 