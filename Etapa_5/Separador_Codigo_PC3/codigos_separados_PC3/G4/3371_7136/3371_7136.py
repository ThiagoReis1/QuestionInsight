u = input("Digite a unidade de medida desejada: K ou M? ")
v = float(input("Digite o valor da medida: "))

if u.upper() == "K" :
	m = v/ 1.60934
else : 
	m = 1.60934 * v
	
print(round(m, 2))