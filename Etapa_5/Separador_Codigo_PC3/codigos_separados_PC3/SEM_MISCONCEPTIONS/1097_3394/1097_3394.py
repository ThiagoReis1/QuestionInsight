numero= int(input("digite o numero:"))
primeira_parte= numero//1000
segunda_parte = numero%1000
condicao= (primeira_parte-segunda_parte)**2


if numero == condicao :
	print("atende")
else:
	print("nao atende")

print(numero)
j