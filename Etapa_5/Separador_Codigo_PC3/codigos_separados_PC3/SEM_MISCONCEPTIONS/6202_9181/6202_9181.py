altura_bia = 1.69
taxa_bia = 0.01
anos = 0

altura_outro = float(input(""))
taxa_outro = float(input(""))

while(altura_outro<altura_bia):
	altura_bia+=taxa_bia
	altura_outro+=taxa_outro
	anos+=1
	print(anos)
	
