x = float(input("x: "))
k = int(input("k: "))
soma = 0
sinal = -1
el = 0
while (el < k ):	
	soma = soma - sinal *(x**el)  
	sinal = -sinal
	el= el+1
print(round(soma,7))
