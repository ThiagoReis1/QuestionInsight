x = int(input())
y = int(input())

soma = 0
t = x
while (t <= y):
	if (t % 7 == 0):
		soma = soma + t
	t = t + 1
		
print(soma)