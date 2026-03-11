from numpy import*
peso = array(eval(input("peso: ")))
altura = array(eval(input("altura: ")))
cont = zeros(3, dtype=float)

for x in range(size(peso)):
	imc = peso[x]/(altura[x]**2)
	if(imc < 17):	
		#cont[0] = cont[0] + 1
		p = "muito abaixo do peso"
	elif(imc <= 17 and imc >= 18.49):
		#cont[1] = cont[1] + 1
		p = "abaixo do peso"
	elif(imc <= 18.5 and imc >= 24.99):
		#cont[2] = cont[2] + 1
		p = "peso normal"
	elif(imc <= 25 and imc >= 29.99):
		#cont[3] = cont[3] + 1
		p = "acima do peso"
	elif(imc <= 30 and imc >= 34.99):
		#cont[4] = cont[4] + 1
		p = "obesidade"
	elif(imc <= 35 and imc >= 39.99):
		#cont[5] = cont[5] + 1
		p = "obesidade severa"
	elif(imc > 40):
		#cont[6] = cont[6] + 1
		p = "obesidade morbida"
	cont[x] = imc	
print(cont)
print("O MAIOR IMC DA TURMA EH:", max(cont).p.upper())

