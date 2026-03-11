x = int(input())
y = int(input())
acumulador = 0
while x <= y:
	if x % 7 == 0:
		acumulador += x
	x += 1
print(acumulador)