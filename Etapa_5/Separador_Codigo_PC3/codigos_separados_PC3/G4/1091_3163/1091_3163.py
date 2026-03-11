nf = int(input(" digite o valor: "))
a1= nf //100
a2= nf % 100
carac = (a1 + a2)**2
print(nf)
if(nf == carac):
	print("atende")
else:
	print("nao atende")
	