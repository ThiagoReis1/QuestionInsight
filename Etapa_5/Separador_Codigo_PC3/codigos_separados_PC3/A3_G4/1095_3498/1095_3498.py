N = int(input("Digite um numero:"))

b=N//1000000
z=b%1000000

f=z//100000
g=f%100000

x=g//10000
h=x%10000

k=h//1000
o=k%1000

i=o//100
p=i%100

w=p//10
m=p%10

v=m//1
j=v%1


c= (b+j)**2
if ( N == c ):
	print(c)
	print("atende")

else:
	print(c)
	print("nao entende")