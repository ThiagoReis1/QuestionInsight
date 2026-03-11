qm=int(input())
qg=int(input())
qr=int(input())
soma=qm
t=0
while(soma>0):
	soma = soma -qg + qr
	t=t+1
print(t)