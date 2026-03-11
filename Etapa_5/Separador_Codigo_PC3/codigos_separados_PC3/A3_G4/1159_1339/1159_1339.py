nit=float(input())
nip=float(input())
tct=float(input())
tcp=float(input())
nme=float(input())


anos=0
soma=0

while(nit and nip < nme):
	nit=nit+(nit*tct)
	nip=nip+(nip*tcp)
	soma=(nit+nip)
	anos=anos+1
print(anos)