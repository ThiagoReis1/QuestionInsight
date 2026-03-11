qi=int(input(""))
qc=int(input(""))
pi=float(input(""))
pc=float(input(""))
b=0
cont=0
while(cont <= 50000):
	if(qi and qc >0):
			a=qi * (pi/100)
			x=qc * (pc/100)
			c=a+x
			cont=c+qi + qc
			cont=cont+c
			
print(cont)	