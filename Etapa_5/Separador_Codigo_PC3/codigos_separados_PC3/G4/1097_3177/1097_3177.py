nf = int(input("digite"))
va = nf//1000
vb = nf % 1000
s = ((va - vb)**2)

if(s == nf):
	print("atende")
else:
	print("nao atende")
print(nf)