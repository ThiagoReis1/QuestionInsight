N = int(input())
contador = 0 
while N != -1:
	if N >= 101 and N <= 201:
		contador = contador + 1
	N = int(input())
print(contador)