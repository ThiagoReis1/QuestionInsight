v = float(input("Valor da mensalidade: "))
n = int(input("numero de criancas: "))
if (n==1):
	t = v - (v/10)
elif (n==2):
	t = 2*v - ((2*v)*(3/10))
else:
	t = (n*v) - ((n*v)*(4/10))
print(round(t ,2))
	