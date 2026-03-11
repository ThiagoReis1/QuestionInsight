v = float(input("Valor do premio: "))
m = float(input("Saque mensal: "))
j = float(input("Insira o valor dos juros: "))

if(v > 0 and m >0 and j >0):
	t = 0
	s = v
	f = v + (v*20)/100
	while(s<=f):
		s = s+((s*j)/100)
		s = s-m
		s = round(s,2)
		t = t+1
	print(t)
else:
	print("Dados incorretos")

	
		

