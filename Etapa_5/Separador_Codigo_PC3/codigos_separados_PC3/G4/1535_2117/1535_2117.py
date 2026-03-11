x=float(input("número real x: "))
k=int(input("quantidade de termos: "))

t=0
sinal=1
e=1
y=0

while(t<k):
	y=y+sinal*((x**e)/e)
	e=e+2
	t=t+1
	sinal=-sinal
print(round(y,6))