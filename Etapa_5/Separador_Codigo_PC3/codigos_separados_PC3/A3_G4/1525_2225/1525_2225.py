v0=int(input("v0: "))
vb=int(input("vb: "))
vr=int(input("vr: "))

i=0
t=0
x=v0
r=vr-vb
while(x>1000):
	x=x-r
	t=t+1
print(t)