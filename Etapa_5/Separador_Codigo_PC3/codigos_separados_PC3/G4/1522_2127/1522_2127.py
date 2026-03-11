qi=int(input("quantidade inicial:"))
qm=int(input("despesa mensal:"))
qmm=int(input("quantidade m:"))
qrm=int(input("quantidade r:"))
k=0
while (qi>0):
	qi=qi-qm+(qmm-qrm)
	k=k+1
print(k)