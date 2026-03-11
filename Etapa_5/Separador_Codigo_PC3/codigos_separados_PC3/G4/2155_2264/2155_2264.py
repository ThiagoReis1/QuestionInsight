from numpy import *
from math import *
p = array(eval(input(": ")))
h = array(eval(input(": ")))
v = zeros(size(p))
for i in range(size(p)):
	v[i] = p[i] / h[i] ** 2
	
print(v[i])
if(max[i] < 17 ):
	print("O MAIOR IMC DA TURMA EH:" ,max[i], "MUITO ABAIXO DO PESO")
elif(max[i]>=17) and (max[i]<= 18.49):
	print("O MAIOR IMC DA TURMA EH:" ,max[i], "ABAIXO DO PESO")
elif(max[i]>=18.5) and (max[i]<=24.99):
	print("O MAIOR IMC DA TURMA EH:" ,max[i], "PESO NORMAL")
elif(max[i]>=25) and (max[i] <=29.99): 
	print("O MAIOR IMC DA TURMA EH:" ,max[i], "ACIMA DO PESO")
elif(max[i]>=30) and (max[i] <=34.99):
	print("O MAIOR IMC DA TURMA EH:" ,max[i], "OBESIDADE")
elif(max[i]>=35) and (max[i] <=39.99):
	print("O MAIOR IMC DA TURMA EH:", max[i], "OBESIDADE SEVERA")
else:
	print("O MAIOR IMC DA TURMA EH: ", max[i], "OBESIDADE MORBIDA")
	
	
	
max(vet)