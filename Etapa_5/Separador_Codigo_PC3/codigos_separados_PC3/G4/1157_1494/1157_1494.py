pi = int(input("Digite a população inicial:"))
txa = float(input("Digite a taxa de crescimento:"))
n = int(input("número de tambaquis retirados anualmente:"))
anos = 0
while (pi > 0):
	pi = pi + ((txa*pi)/100)
	pi = pi - n
	anos = anos + 1
print(anos)
