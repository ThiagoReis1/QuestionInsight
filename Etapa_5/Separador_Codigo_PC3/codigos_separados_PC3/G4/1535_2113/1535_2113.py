x=float(input("numero: "))
k=int(input("numero: "))

t=0
sinal=1
e=1
y=0

while(t<k):
	x=x-(x**3/3)+(x**5/5)-(x**7/7)+(x**9/9)
	y=y+1
	t=t+1
e=e*sinal
print(k)
	