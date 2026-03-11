# faça seu código aqui!
p = int(input("numero de pizzas:"))
if p<3:
	t= 5.00*p+3.00
elif p==3:
	t=5.00*p+3.25
else:
	t=5.00*p+4.50
print(round(t,2))