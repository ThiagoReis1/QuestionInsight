v = float(input("Digite o valor da mensalidade: "))
n = int(input("Digite o numero de criancas: "))
 
if (n == 1):
   valor = v*(c * 0.10)
	print(round(valor, 2))	
elif (n == 2):
   valor = v  * 0.30
	print(round(valor, 2))
elif (n >== 3):
   valor = v * 0.40
	print(round(valor, 2))

	

	
   