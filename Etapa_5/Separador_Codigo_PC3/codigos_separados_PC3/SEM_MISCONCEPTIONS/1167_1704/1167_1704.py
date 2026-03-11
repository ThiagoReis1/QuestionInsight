#n e o numero de aproximacoes
n = int(input("Digite o valor do termo: "))
i = 0
S = 0

# Para alternancia de sinal
sinal = -1

while (i < n):
	denom = (7 + (2*i-1))
	S = S + sinal*(i**2) /denom
	sinal = -sinal
	i = i + 1
	
print(round(S, 11)

#(7 * i + 2)

#print(round(1**2 / (7 + 1), 11)) 