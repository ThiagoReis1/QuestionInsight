N = int(input("termos: "))
cont = 1
div = 3
sinal = -1
S = 0
while (cont<=N):
	S = S + sinal * (cont**2)/(5+div)
	sinal = - sinal
	cont = cont + 1
	div = div +2
print(round(S,10))