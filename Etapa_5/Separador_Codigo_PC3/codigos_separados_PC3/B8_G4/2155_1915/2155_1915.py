from numpy import*
peso = array(eval(input("digite o peso: ")))
alt = array(eval(input("digite a altura: ")))
imc = zeros(size(peso))
k = 0
for i in range(size(peso)):
	imc[k] = round((peso[i]/alt[i]**2),2)
	k = k + 1
print(imc)
print("O MAIOR IMC DA TURMA EH:", max(imc))
imc1 = max(imc)
if(imc1 < 17):
	print("MUITO ABAIXO DO PESO")
elif(imc1 > 17) and (imc1 < 18.49):
	print("ABAIXO DO PESO")
elif(imc1 > 18.5) and (imc1 < 25.99):
	print("PESO NORMAL")
elif	(imc1 > 25) and (imc1 < 29.99):
	print("ACIMA DO PESO")
elif (imc1 > 30) and (imc1 < 34.99):
	print("OBESIDADE")
elif (imc1 > 35) and (imc1 < 39.99):
	print("OBESIDADE SEVERA")
elif( imc1 > 40):
	print("OBESIDADE MORBIDA")