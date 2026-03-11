from numpy import*
ent= input("ENTRADA: ").split(",")
#ent=en.slipt(",")
B=0
PA=0
PR=0
A=0
I=0


for i in range(len(ent)):
	if(ent[i]=="B"):
		B=B+1
	if(ent[i]=="PA"):
		PA=PA+1
	if(ent[i]=="PR"):
		PR=PR+1
	if(ent[i]=="A"):
		A=A+1
	if(ent[i]=="I"):
		I=I+1

saida=zeros(5,dtype=int)

for i in range(size(saida)):
	saida[0]=B
	saida[1]=PA
	saida[2]=PR
	saida[3]=A
	saida[4]=I

print(max(B,PA,PR,A,I))
print(saida)