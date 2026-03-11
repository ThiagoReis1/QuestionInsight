pi = int(input(""))
taxa = int(input(""))
zl = int(input(""))
anos = 0
retirada = 500
while(pi > 0):
	pi = pi + ((taxa/100) * pi)
	pi = pi - zl - retirada
	anos = anos + 1
print(anos)