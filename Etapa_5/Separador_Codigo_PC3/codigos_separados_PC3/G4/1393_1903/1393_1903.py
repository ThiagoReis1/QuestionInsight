p = float(input("Digite o peso da encomenda em gramas: "))

a = p*0.05

b = p*0.04 + 60

if(p<5000):
	print(round(a,2))
else:
	print(round(b,2))