qi=int(input("Digite um numero: "))
dm=int(input("Digite um numero: "))
qm=int(input("Digite um numero: "))
qr=int(input("Digite um numero: "))
meses=0
soma=0
while(qi>0):
	qi=qi-dm+qm-qr
	meses=meses+1
print(meses)