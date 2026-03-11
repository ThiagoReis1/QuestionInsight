altura_bia = 1.69
taxa_bia = 0.01

al = float(input("altura da bia:"))
tx = float(input("taxa: "))

anos = 0

while al <= altura_bia:
	altura_bia +=taxa_bia
	al += tx
	anos += 1
	
print (anos)
	