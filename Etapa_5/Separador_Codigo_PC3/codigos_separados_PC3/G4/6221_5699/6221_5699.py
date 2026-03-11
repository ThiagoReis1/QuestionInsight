x = int(input())
y = int(input())
soma = 0

while x <= y:
	if x%7==0:
		soma += x
	x+=1

print(soma)