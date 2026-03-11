##

a=float(input('Valor do produto:'))

##
b=(5/100*a)
c=(15/100*a)

p=(b+a)
d=(c+a)
##
if(a<=100.00):
	print(round(p,2),'ryous')
	print('Aumento de 5 porcento')
	
else:
	print(round(d,2),'ryous')
	print('Aumento de 15 porcento')