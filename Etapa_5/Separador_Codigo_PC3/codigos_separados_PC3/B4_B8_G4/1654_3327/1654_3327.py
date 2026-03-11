from numpy import*
vet=input("").split(',')
am=0
pe=0
mg=0
sp=0
rs=0
for i in range(len(vet)):
	if vet[i]=="AM":
		am=am+1
	elif vet[i]=="PE":
		pe=pe+1
	elif vet[i]=="MG":
		mg=mg+1
	elif vet[i]=="SP":
		sp=sp+1
	elif vet[i]=="RS":
		rs=rs+1
if am>pe and am> mg and am> sp and am> rs:
	print(am)
elif pe>am and pe> mg and pe> sp and pe> rs:
	print(pe)
elif mg>am and mg> pe and mg> sp and mg> rs:
	print(mg)
elif sp>am and sp> mg and sp> pe and sp> rs:
	print(sp)
elif rs>am and rs> mg and rs> sp and rs> pe:
	print(pe)

vet2=zeros(5,dtype=int)
for i in range(len(vet)):
	if vet[i]=="AM":
		vet2[0]=vet2[0]+1
	elif vet[i]=="PE":
		vet2[1]=vet2[1]+1
	elif vet[i]=="MG":
		vet2[2]=vet2[2]+1
	elif vet[i]=="SP":
		vet2[3]=vet2[3]+1
	elif vet[i]=="RS":
		vet2[4]=vet2[4]+1
print(vet2)