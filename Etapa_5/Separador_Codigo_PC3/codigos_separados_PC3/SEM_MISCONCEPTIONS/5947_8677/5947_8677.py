salgado = input("Escolha (C) Coxinha ou (E) esfirra: ")
qtdd = int(input("Insira a quantidade: "))
qsucos = int(input("Insira a quantidade de sucos: "))

if salgado == "C":
	total = (qtdd * 2.0) + (qsucos * 6.0)
else:
	total = (qtdd * 4.50) + (qsucos * 6.0)
print(round(total, 2))