E = float(input("Digite o numero de horas extras: "))
F = float(input("horas que o funcionario faltou: "))

H = E - (2 / 3) * F
print("Entradas: " , E , "horas extras e", F ,"horas de falta")

if(H < 0 or E < 0 or F < 0):
	gratificacao = -1
elif(H > 2400):
	gratificacao = 500.00
elif(H > 1800 and H <= 2400):
	gratificacao = 400.00
elif(H > 1200 and H <= 1800):
	gratificacao = 300.00
elif(H > 600 and H <= 1200):
	gratificacao = 200.00
elif(H <= 600):
	gratificacao = 100.00
if(gratificacao == -1):
	print("Dados invalidos")
else:
	print("Gratificacao: R$",round(gratificacao, 2))
	
	
		


	