n = int(input())
soma = 0

while(n != -1):
	if(n >= 26) and (n <= 85):
		soma += 1
	n = int(input())
print(soma)