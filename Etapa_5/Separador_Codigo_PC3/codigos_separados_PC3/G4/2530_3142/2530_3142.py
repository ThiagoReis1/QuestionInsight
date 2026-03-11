D = float(input(""))
TF = float(input(""))
J = float(input("")) / 100

m = 0
s = D 

if(D > 0 and TF > 0 and J > 0):
	while(s <= 0.15 * D + D):
		s = s + (J * s) - TF
		m = m + 1
	print(m)
else:
	print("Dados incorretos")
	
