soma = 0
x = float(input())
k = int(input())
soma += x
for i in range(1,k):
	soma+= x**(i*2+1)/(i*2+1)
print(round(soma,7))