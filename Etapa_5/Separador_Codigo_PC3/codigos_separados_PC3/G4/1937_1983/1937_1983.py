na = input("alanina / valina: ").upper()
o=15.9994
c=12.011
n=14.00674
h=1.00794
if(na=='ALANINA'):
	mensagem =((3*c)+(h*7)+n+(o*2))
	print(round(mensagem,2))
else:
	mensagem = ((c*5)+(h*11)+n+(o*2))
	print(round(mensagem,2))