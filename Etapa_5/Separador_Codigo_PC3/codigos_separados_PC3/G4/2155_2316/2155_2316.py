from numpy import*
vet = array(eval(input()))
vet2 = array(eval(input()))
vet3 = zeros(size(vet),dtype=float)

j = 0
for i in vet:
	vet3[j] = round(i/(vet2[j]*vet2[j]),2)
	j = j + 1
print(vet3)
print("O MAIOR IMC DA TURMA EH: ",round(max(vet3),2))

if (max(vet3) <17):
	print("MUITO ABAIXO DO PESO")
if (max(vet3) >= 17 and max(vet3) <= 18.49):
	print("ABAIXO DO PESO")
if (max(vet3) >=18.5 and max(vet3) <= 24.99):
	print("PESO NORMAL")
if (max(vet3) >=25 and max(vet3) <= 29.99):
	print("ACIMA DO PESO")
if (max(vet3) >=30 and max(vet3) <= 34.99):
	print("OBESIDADE")
if (max(vet3) >=35 and max(vet3) <= 39.99):
	print("OBESIDADE SEVERA")
if (max(vet3) >=40):
	print("OBESIDADE MORBIDA")