c =float(input(""))
vi=float(input(""))
dm=float(input(""))
tjuros=float(input(""))
t=0
a=c
b=vi
e=dm
j=tjuros/100
i= b+e+(b*j)
while(a>=i):
	if(a>0 and b>0 and e>0 and j>0):
		t=t+1
	else:
		print("Dados incorretos")
print(t)
