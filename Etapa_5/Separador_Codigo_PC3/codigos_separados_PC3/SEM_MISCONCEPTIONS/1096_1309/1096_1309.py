X= int(input("digite um numero X:"))

p= X//10000
resto_p= X%10000

s= resto_p//100
resto_s=resto_p%100

t=resto_s

soma_c = p**3 + s**3 + t**3

if(X==soma_c):
	print(X,"atende a propriedade")
else:
	print(soma_c)
	