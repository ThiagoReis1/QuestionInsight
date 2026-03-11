n = int(input())
a = n//10000
a1 = n%10000
b = a1//100
b1 = b%100
c = b1

soma = a**3 + b**3 + c**3
if(a**3 + b**3 + c**3  == n):
	print( n, "atende a propriedade")
else:
	print(soma)