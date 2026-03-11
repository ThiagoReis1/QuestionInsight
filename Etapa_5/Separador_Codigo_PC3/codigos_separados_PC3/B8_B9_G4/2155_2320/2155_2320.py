from numpy import*
peso= array(eval(input("Digite seu peso:")))
altura = array(eval(input("Digite a sua altura:")))

var1 = zeros(size(peso),dtype=float)

for i in range(size(peso)):
	var1[i] = round(peso[i]/(altura[i]*altura[i]),2)

print(var1)
print("O MAIOR IMC DA TURMA EH:",round(max(var1),2))
var = max(var1)

if(var < 17.0):
	 print ("MUITO ABAIXO DO PESO")
	
elif var >= 17 and var<= 18.49:
	 print("ABAIXO DO PESO")
	
elif var >= 18.5 and var<= 24.99:
	 print("PESO NORMAL")
		
elif var >= 25 and var <= 29.99:
	 print("ACIMA DO PESO")

elif var >= 30 and var <= 34.99:
	 print ("OBESIDADE")
	
elif var >= 35 and var <=39.99:
	print ("OBESIDADE SEVERA")
	
elif var >= 40:
	print ("OBESIDADE MORBIDA")