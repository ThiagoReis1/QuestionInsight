nit=int(input())
nip=int(input())
tat=float(input())
tap=float(input())
tot=int(input())
t=1
while((nit+nip)<=tot):
	nit=(nit + nit*(tat/100))*t
	nip=(nip + nip*(tap/100))*t
	t=t+1
print(t)