# faça seu código aqui!
np = int(input('Informe o nnumero de pizzas: '))
tx1 = 3.
tx2 = 3.25
tx3 = 4.5
ent = 5.0
total = 0.

if(np < 3):
	print(round(np * ent + tx1,2))
elif(np == 3):
	print(round(np * ent + tx2,2))
else:
	print(round(np * ent + tx3,2))
