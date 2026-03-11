nf=int(input("numero fornecido:"))
n1=nf//1000
n2=nf%1000
n3 =((n1-n2)**4) 
if(n3==nf):
	print(nf)
	print("atende")
else:
	print(nf)
	print("nao atende")
	
