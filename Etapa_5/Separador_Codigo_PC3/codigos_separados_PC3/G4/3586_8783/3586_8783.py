from numpy import *
anel=array(eval(input("insira:")))
i=0
pont=0
while i<size(anel):
	if anel[i]==1:
		pont=pont+100
	if anel[i]==2:
		pont=pont+60
	if anel[i]==3:
		pont=pont+20
	if anel[i]==4:
		pont=pont+0
	i+=1
print(pont)