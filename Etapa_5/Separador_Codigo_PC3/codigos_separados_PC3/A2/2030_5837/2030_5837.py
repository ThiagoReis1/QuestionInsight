moeda=(input("Lado da moeda: ")).upper()
a=0

while moeda!="S":
	if moeda=="CARA":
		a=a+1
	else:
		a=a
	moeda=(input("Lado da moeda: ")).upper()
print(a)