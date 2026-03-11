habitantes = int(input("N de habitantes: "))
vampiros = int(input("Vampiros: "))
trans = int(input("Trans/dia: "))
mortos = int(input("Vampiros cacados: "))
cap = vampiros * trans
cont = 1
while (habitantes > 0):
	vampdia = vampiros*trans) - mortos
	print ("vampdia",vampdia)
	vampiros = vampiros + vampdia
	print ("vampiros",vampiros)
	habitantes = habitantes - vampiros
	cont = cont+1
print(cont)