from math import*
x = eval(input("Digite o angulo: "))
k = int(input("numero de termos: "))
cos = 1
nt = 2
if (k ==1):
	cos = cos
while (nt <= k):
	t = (-((-1)**nt)*(x**(2*nt -2)))/factorial(2*nt - 2)
	cos = cos + t
	nt = nt + 1
print(round(cos,10))