N = int(input())
saida = []

for i in range(N + 1):
		
		if N < i: break
		else:
			print(N - i)
			N -= 2
			
print('Fim da contagem regressiva!')