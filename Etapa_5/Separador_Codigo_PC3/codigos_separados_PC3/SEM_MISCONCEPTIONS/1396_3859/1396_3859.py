##Restaurante Bucho Cheio

valorconsu = float(input("Qual o valor consumido no resturante? "))

##Condicao 300 ou < que isso 10% do garcon

if (valorconsu <= 300.0):
	garcon = valorconsu*0.10
	total = (valorconsu + garcon)

## Condicao > 300 6% do garcon
else:
	garcon = valorconsu*0.06
	total = (valorconsu + garcon)

print(round(total,2))