x = float(input())
n = int(input())

soma = 0 
i = 0

while(i < n):
	soma = soma + x/(i*2+1)
	i = i + 1
print(round(soma, 8))