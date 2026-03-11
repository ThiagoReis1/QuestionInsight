# faça seu código aqui!
x = float(input("idade: "))
pf = 20.00

if x < 12:
	total = pf + 1.25
elif x == 12:
	total = pf + 2.25
elif x > 12:
	total = pf + 3.25
	
print(round(total, 2))