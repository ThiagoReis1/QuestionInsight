coxinha = 2.00
esfirra = 4.50
suco = 6.00

x = input("digite 'C' para coxinha ou 'E' para esfirra: ").upper()
lanches = int(input("digite a quantidade de coxinhas ou esfirras: "))
qtsucos = int(input("digite a quantidade de sucos: "))

if x == 'C':
	total = (lanches*coxinha) + (qtsucos*suco)

elif x == 'E':
    total = (lanches*esfirra) + (qtsucos*suco)
	
else:
	print("Tipo de lanche invalido.")
	
print(round(total, 2))