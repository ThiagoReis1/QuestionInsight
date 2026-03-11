x = int(input("numero x : "))
y = int(input("numero y : "))

soma = 0
while( x <= y ) :
	if (x % 2) == 0 :
		soma += x
	x += 1
print(soma)