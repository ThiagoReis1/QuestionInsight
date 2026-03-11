# faça seu código aqui!
dias = int(input())

if dias < 15:
	diaria = (175 * dias) + 20
	print(round(diaria,2))
elif dias > 15:
	diaria = (175 * dias) + 10
	print(round(diaria,2))
elif dias == 15:
	diaria = (175 * dias) + 16
	print(round(diaria,2))