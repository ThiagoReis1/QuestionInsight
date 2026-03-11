x=float(input("Valor: "))
k=int(input("Quantidade de termos: "))

t=0

total=x*t

while k != t:
	t=t+1
	total=total+(x/(2*t))
print(round(total,8))