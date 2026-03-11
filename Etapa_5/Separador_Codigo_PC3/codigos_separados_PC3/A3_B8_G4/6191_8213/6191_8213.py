x=input("Digite a face da moeda:")
cara=0
cont=0
while x.upper!="s":
	x=input("Digite a face da moeda:")
	if x.upper=="cara":
		cara==cara+1
	elif x.upper=="S":
		print(cara)
