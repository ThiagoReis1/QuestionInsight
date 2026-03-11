# faça seu código aqui!
qnt_p = int(input("Quantidade de pecas: "))
fixo = 30

if qnt_p < 10:
	total = fixo + 3.25
elif qnt_p == 10:
	total = fixo + 4.50
else:
	total = fixo + 6.00
print("total=", round(total, 2))