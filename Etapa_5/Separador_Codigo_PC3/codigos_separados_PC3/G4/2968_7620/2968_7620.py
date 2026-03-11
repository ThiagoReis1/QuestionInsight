##

a=input('L para lanche ou S para salgados:').upper()
b=int(input('Quantidade de lanches ou salgados:'))
c=int(input('Quantidade de refrigerantes:'))

##
d=5.00
s=3.50
r=4.00
j1=(b*s+r*c)
p1=(b*d+r*c)

##
if(a=='L'):
	m=p1
	
else:
	m=j1
##

print(round(m,2))