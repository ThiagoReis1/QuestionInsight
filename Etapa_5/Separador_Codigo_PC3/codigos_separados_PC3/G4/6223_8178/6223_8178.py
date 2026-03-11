x = int(input("insira um numero"))
y = int(input("insira um numero"))
soma = 0

if x % 2 == 0:
	x += 1
while x <= y:
	soma += x
	x += 2
print(soma)
