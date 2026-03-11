#Universidade Federal do Amazonas
#Fernanda Bonfim - 21602340

qtd = int(input("Quantidade inicial de tambaquis: "))
i = float(input("Taxa anual de crescimento: "))
retirados = int(input("Quantidade retirada por ano de tambaquis: "))
x = 0

while(qtd > 0):
	qtd = qtd + ((qtd *  i)/100)
	qtd = qtd - retirados
	x = x + 1
print (x)