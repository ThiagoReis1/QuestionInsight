c=float(input("c?"))
d=float(input("d?"))
m=float(input("m?"))
j=float(input("j?"))
t=0
s=d
k=1+(j/100)

if(c>0)and(d>0)and(m>0)and(j>0):
	while(s<c):
		s=s*k
		s=round(s,2)
		s=s+m
		s=round(s,2)
		t=t+1
	print(t)
else:
	print("Dados incorretos")
	