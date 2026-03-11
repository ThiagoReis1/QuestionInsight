nf= int(input("numero fornecido:"))
n1= nf//100
n2= nf % 100

if ((n1+n2)**2)==nf:
	m= "atende"
else:
	m= "nao atende"

print(nf)
print(m)