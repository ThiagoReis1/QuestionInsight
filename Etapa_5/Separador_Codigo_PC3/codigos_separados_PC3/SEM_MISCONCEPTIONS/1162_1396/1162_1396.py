premio = int(input("Digite o valor do premio: "))
taxader = float(input("Digite a taxa de rendimento: "))
gastos = int(input("Digite o dinheiro gasto: "))
a = 1

while ( gastos <= premio):
	a = a + 1
	m = (m * a /12 ) + (premio - (gastos * taxader))
   print (a )