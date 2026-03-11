aminohcl = input("Digite o amino acido:")
O = float(15.999)
C = float(12.011)
N = float(14.00674)
H = float(1.00794)

if (aminohcl.lower() == "histidina"):
	peso = (6*C)+(10*H)+(3*N)+(2*O)
	print(round(peso,2))
else:
	peso = (5*C)+(10*H)+(N)+(2*O)
	print(round(peso,2))