x = float(input())
k = int(input())

n = 1
y = 0

while(k > 0):
	act = (x**n)/n
	soma = act + y
	y = soma
	k = k - 1
	n = n + 2

print(round(soma,7))