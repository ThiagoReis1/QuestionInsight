# faça seu código aqui!

x = int(input(":"))
taxa = 5.00

if x < 3:
	f = (x * taxa) + 3.00 
elif x == 3:
	f = (x * taxa) + 3.25
elif x > 3:
	f = (x * taxa) + 4.50
print(round(f,2))