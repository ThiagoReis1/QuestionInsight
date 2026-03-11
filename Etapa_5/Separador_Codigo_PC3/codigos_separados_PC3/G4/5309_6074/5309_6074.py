x = float(input())
k = int(input())

i = 1
soma = 0

while(i <= k):
	soma += x/(2*i-1)
	i = i + 1
print(round(soma,8))