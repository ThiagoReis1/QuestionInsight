copinicial = int(input("No. de copias inicias:"))
taxa = int(input("taxa de reducao semanal:"))
copintrod = int(input("No. de copias introduzidas:"))
contador = 0
soma = copinicial
while (soma <= 1000000):
	soma = (soma - (soma*taxa/100)) + copintrod
	contador = contador + 1
print(contador)
