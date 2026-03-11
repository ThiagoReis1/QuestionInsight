from numpy import*
v=input("vetor").upper().split(',')
copia= zeros(5,dtype=int)
for x in v:
	if x=="BE":
		copia[0]=copia[0]+1
	elif x=="ES":
		copia[1]=copia[1]+1
	elif x=="FR":
		copia[2]=copia[2]+1	
	elif x=="IT":
		copia[3]=copia[3]+1	
	elif x=="PT":
		copia[4]=copia[4]+1	
print(max(copia))
print(copia)