u = input("Digite a unidade: ").lower()
v = float(input("Digite o valor da medida: "))
if u == "k" :
	m = v/1.60934
	print(round(m,2))
else:
	h = 1.60934*v
	print(round(h,2))
	