n = int(input())

soma = 0
i = 0

while(n != -1):
	soma = soma + 1
	if(n == 6):
		i = i + 1
	n = int(input())
p = i*100/soma	
print(soma)
print(round(p, 2))


