from numpy import *
face= array(eval(input('digite as faces que cairam: ')))
i= 0
total= 0

while (i<size(face)):
	if (face[i]==1):
		total= total+10
		i= i+1
	elif (face[i]==2):
		total= total+5
		i= i+1
	elif (face[i]==3):
		total= total+0
		i= i+1
	elif (face[i]==4):
		total= total+5
		i= i+1
	elif (face[i]==5):
		total= total+20
		i= i+1
	elif (face[i]==6):
		total= total+10
		i= i+1

print(total)