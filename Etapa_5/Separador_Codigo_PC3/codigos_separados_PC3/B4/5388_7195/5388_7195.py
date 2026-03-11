from numpy import*

pal=input("").upper()
i=0
total=0
while i < len(pal):
	if pal[i]=="A":
		total=total+25.12
		
	elif pal[i]=="E":
		total=total+25.12
		
	elif pal[i]=="I":
		total=total+25.12
		
	elif pal[i]=="O":
		total=total+25.12
	elif pal[i]=="U":
		total=total+25.12
	else:
		total=total+40.18
	i=i+1	
		

print(round(total,2))