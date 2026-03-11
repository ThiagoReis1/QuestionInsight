x = int(input())
y = int(input())
soma = 0
for i in range(x,y+1):
	if i%2!=0:
		soma +=i
print(soma)