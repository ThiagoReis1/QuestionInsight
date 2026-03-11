x = float(input("Numero real x:"))
k = int(input("Quant de termos:"))
soma = 0
t = 1
while (x>-1) and (x<=1) and (t<=k) and (k>0):
	soma = soma - (((-1)**t)*x**t)/t
	t = t+1
print(round(soma,10))