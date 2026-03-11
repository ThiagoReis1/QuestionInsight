from numpy import*

p = input("Palavras: ")

i=0
x=0
while i<len(p):

	if p[i]== 'A':
		x=x+45.12
		
	elif p[i]=='E':
		x=x+45.12

	elif p[i]=='I':
		x=x+45.12
		
	elif p[i]=='O':
		x=x+45.12
	
	elif p[i]=='U':
		x= x+45.12
		
	else :
		x = x+50.18
		
	i = i +1

print(round(x,2))
