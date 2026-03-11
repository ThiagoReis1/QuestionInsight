# faça seu código aqui!
me = int(input("Quantidade de manhas energeticas: "))

total = 20 * me

if (me >= 4):
	conta = total - (total*(15/100))
else:
	conta = total
print (round(conta,2))