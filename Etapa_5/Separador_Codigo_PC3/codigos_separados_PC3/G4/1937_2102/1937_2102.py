nome=input()

O=15.9994
C=12.011
N=14.00674
H=1.00794

conta=(3*C)+(7*H)+N+(2*O)
c2=(5*C)+(11*H)+N+(2*O)

if(nome=="Alanina".upper()):
	print(round(conta,2))
else:
	print(round(c2,2))