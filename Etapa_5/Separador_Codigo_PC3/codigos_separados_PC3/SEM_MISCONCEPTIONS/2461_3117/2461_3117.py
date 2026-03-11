preco = float(input("lsdkfh: "))

if preco <= 50:
	sai = preco + preco
elif preco >= 50.01 and preco <= 100:
	sai = preco + (preco / 2)
elif preco >= 100.01 and preco <= 500:
	sai = preco + (preco * 0.4)
else:
	sai = preco + (preco * 0.3)

print(round(sai,2))	