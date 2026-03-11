# faça seu código aqui!
q = int(input("quantidade de pizzas "))
if q < 3 :
	r = q * 5 + 3
elif q == 3 :
	r = q * 5 + 3.25
elif q > 3:
	r = q * 5 + 4.50
print("total=",round(r,2))