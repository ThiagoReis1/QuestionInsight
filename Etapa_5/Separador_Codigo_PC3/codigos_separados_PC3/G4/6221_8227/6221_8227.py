X = int(input("Digite valor de X:"))
Y = int(input("Digite valor de Y:"))

soma = 0
 
for num in range (X,Y+1):
	if num % 7 == 0:
		soma += num 
print(soma)