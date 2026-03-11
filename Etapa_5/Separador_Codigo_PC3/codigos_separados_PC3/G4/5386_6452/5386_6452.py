from numpy import*
g= input('digite a palavra: ').upper()
a=0
b=0
x=0
while a <len(g):
	if g[a]== "A" or g[a]== "O" or g[a]=="E" or g[a]=="I" or g[a]=="U":
		x=x+1.12
	else:
		b=b+1.18
	a=a+1
ct=x+b
print(round(ct,2))
		
	
