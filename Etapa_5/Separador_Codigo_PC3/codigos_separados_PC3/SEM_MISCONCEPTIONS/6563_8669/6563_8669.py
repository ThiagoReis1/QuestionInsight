# faça seu código aqui!
dias= int(input("dias: "))

if dias < 15:
	valor= (175*dias)+20
elif dias == 15:
	valor= (175*dias)+16
else:
	valor= (175*dias)+10

total=valor
print("total=", total)
