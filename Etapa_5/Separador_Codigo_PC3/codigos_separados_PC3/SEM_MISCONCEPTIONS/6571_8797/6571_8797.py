# faça seu código aqui!
p = float(input("pacote: "))

taxa = 10

if p<5:
	p = 3.75
	total = p + taxa 
elif p == 5:
	p = 4.75
	total = p + taxa 
else: 
	p > 5
	p = 5.75
	total = p + taxa 
print("total=", round(total, 2))