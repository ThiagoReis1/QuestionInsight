x = int(input())
y = int(input())

i = x

soma = 0

while(i<=y):
	if i % 2 == 1:
		soma =soma+i
	i = i + 1
	
print(soma)