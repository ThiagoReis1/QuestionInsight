altura_bia = 1.69
taxa_bia = 0.01
anos = 0

alt= float(input("altura:"))
txc = float(input("taxa de crescimento:"))

while alt < altura_bia:
	altura_bia = altura_bia + taxa_bia
	alt = alt + txc
	anos = anos +1

print(anos)	
	
	
	
	