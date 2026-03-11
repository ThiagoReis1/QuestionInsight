from numpy import*
prod = input("insira os produtos: ").upper()

i = 0  #contadora
total = 0   #total da compra
k = 0
k2 = 0
k3 = 0

while i < len(prod):
	if prod[i] == "I":
		k += 1
	elif prod[i] == "M":
		k2 += 1
	elif prod[i] == "S":
		k3 += 1
	i += 1
total = (k * 3.75) + (k2 * 4.50) + (k3 * 2.90)
print(round(total, 2))
	
		
		
	