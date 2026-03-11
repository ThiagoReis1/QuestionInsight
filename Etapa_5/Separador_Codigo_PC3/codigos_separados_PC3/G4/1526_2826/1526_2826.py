qi=int(input("quantidade inicial: "))
gp=int(input("gasta por dia: "))
rs=int(input("recupera pos sono: "))
t=0

while(qi>0):
	qi=qi+rs-gp
	t=t+1
print(t)