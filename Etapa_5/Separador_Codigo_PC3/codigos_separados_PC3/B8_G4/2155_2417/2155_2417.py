from numpy import *
peso = array(eval(input("")))
altura = array(eval(input("")))
cont = zeros(size(peso), dtype = float)
for i in range(size(peso)):
	cont[i] = round(peso[i] / (altura[i]) ** 2, 2)
print(cont)
print("O MAIOR IMC DA TURMA EH:", max(cont))

if max(cont) < 17:
	msg = "MUITO ABAIXO DO PESO"
elif (max(cont) >= 17) and max(cont) <= 18.49:
	msg = "ABAIXO DO PESO"
elif (max(cont) >= 18.5) and max(cont) <= 24.99:
	msg = "PESO NORMAL"
elif (max(cont) >= 25) and max(cont) <= 29.99:
	msg = "ACIMA DO PESO"
elif (max(cont) >= 30) and max(cont) <= 34.99:
	msg = "OBESIDADE"
elif (max(cont) >= 35) and max(cont) <= 39.99:
	msg = "OBESIDADE SEVERA"
elif max(cont) > 40:
	msg = "OBESIDADE MORBIDA"
print(msg)





