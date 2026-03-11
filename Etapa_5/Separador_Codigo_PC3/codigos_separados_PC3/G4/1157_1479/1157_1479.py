pi = int(input("Digite a população inicial: "))
taxa = float(input("Digite a taxa: "))
n = int(input("Numero de tambaquis retirados: "))
anos = 0

while(pi > 0):
	pi = pi + ((taxa*pi)/100)
	pi = pi - n
	anos = anos + 1
print(anos)