from numpy import*

vc= array(eval(input("Digite: ")))

i= 0
valor= 0

while (i < size(vc)):
	if vc[i] > 80:
		valor= valor + ((vc[i] - 0,8))
	else:
		valor= valor + vc[i]
	i= i + 1
print(round(valor, 2))