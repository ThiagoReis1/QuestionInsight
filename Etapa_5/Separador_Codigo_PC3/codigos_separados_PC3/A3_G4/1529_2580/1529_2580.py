i=int(input("quantidade infantaria: "))
c=int(input("quantidade cavalaria: "))
i1=float(input("percentual infantaria: "))
c1=float(input("percentual cavalaria: "))
Q0=i
Q1=c
meses=0
while(i<25000 and c<25000):
	i=i+(i*i1/100)
	c=c+(c*c1/100)
	meses=meses+1
print(meses)