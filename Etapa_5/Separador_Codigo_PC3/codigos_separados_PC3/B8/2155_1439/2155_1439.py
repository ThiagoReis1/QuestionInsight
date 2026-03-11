from numpy import*
peso = array(eval(input("digite o peso:")))
altura = array(eval(input("digite a altura: ")))
for i in size(peso):
	imc = peso[i]/altura[i]
	print(round(imc,2))
	print("O MAIOR IMC DA TURMA EH:",max(imc))
	if (max(imc) < 17 ):
		print("MUITO ABAIXO DO PESO")
	elif (max(imc) > 17)and(max(imc) < 18.49):
		print("ABAIXO DO PESO")
	elif (max(imc) > 18.5)and(max(imc) < 24.99 ):
		print("PESO NORMAL")
	elif (max(imc) > 30)and(max(imc) < 34.99):
		print("OBESIDADE")
	elif (max(imc) > 35)and(max(imc) < 39.99):
		print("OBESIDADE SEVERA")
	elif (max(imc) > 40):
		print("OBESIDADE MORBIDA")