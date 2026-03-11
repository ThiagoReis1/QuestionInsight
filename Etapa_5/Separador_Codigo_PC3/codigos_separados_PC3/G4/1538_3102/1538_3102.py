x = float(input("numero real x :"))
k = int(input("numero de termos da serie:"))
t = 0
i = 0
soma = 0 
sinal = 1

while(t<k):
	soma = soma + (x**i)*sinal
	i = i + 2
	sinal = -sinal
	t = t + 1
print(round(soma,8))
	
	