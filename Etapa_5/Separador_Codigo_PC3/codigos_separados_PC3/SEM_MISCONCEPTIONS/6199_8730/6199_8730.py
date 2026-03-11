altura_cicero = 1.8
taxa_cicero = 0.01
alt =  float(input("altura:"))
tx = float(input("taxa de crescimento:"))
anos = 0
while alt <altura_cicero:
	altura_cicero+=taxa_cicero
	alt+=tx
	anos+=1
print(anos)