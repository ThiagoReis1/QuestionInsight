x = float(input("Digite um numero real x: "))
k = int(input("Digite um numero de termos k: "))
c=1
y=0
t=1
v=0
while(c<=k):
	y = y + t*(x**v)
	t = t*(-1)
	v = v+1
	c = c+1
print(round(y,7))