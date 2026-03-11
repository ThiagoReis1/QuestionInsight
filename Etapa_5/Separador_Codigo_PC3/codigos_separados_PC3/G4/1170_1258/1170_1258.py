N = int(input("digite o inteiro:"))
i = 0
se = -N
sinal = 1
while(i<=N):
	x = sinal*pow(N+1,3)/7
	se = se + x
	i = i +1 
	sinal = -sinal 
print(round(se,7))