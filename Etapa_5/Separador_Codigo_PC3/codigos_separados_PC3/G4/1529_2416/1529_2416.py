qi=int(input("No. guerreiros infantaria: "))
qc=int(input("No. guerreiros cavalaria: "))
i=0
c=0
m=0
pi=qi*3/100
pc=qc*4/100
while (i and c <=50000):
	i=i+qi+pi
	c=c+qc+pc
	m=m+1
print(m)	
	