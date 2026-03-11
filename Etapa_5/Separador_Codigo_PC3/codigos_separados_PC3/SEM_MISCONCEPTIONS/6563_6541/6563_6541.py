dias = int(input())

if dias < 15:
	taxa = 20
elif dias == 15:
	taxa = 16
else:
	taxa = 10
	
valor = (dias * 175) + taxa

print("total= {:.0f}".format(valor))
