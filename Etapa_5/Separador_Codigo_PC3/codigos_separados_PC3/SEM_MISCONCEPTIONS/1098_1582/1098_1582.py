numero = int(input("insira o numero"))

part1 = numero // 1000
part2 = numero % 1000
valor = (part1 - part2)**4

if( numero == valor ):
	print(numero, "atende a propriedade")
	
else:
	print(valor)
