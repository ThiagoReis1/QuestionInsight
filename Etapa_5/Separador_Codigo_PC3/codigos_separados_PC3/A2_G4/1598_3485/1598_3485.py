from numpy import*

vet = array(eval(input("Digite o valor da compra: ")))

for x in vet:
	if(x > 80.0):
		x = x - 5
	else:
		x = x
		
	s = sum(vet)
print(round(s, 2))