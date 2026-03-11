# faça seu código aqui!

base_price = 50.0

dist = int(input())
taxa = 0

if dist == 10:
	taxa = 7.75
elif dist > 10:
	taxa = 10.0
else:
	taxa = 5.5

total = base_price + taxa

print('total=', round(total, 2))