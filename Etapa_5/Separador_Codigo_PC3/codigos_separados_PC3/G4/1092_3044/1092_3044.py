x=int(input("numero: "))
a=x//100
b=(x//10)%10
c=x%10
s=(a**3)+(b**3)+(c**3)
if(s==x):
	m="atende"
else:
	m="nao atende"
print(x)
print(m)