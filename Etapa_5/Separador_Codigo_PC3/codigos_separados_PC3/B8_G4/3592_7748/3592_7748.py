from numpy import*

pts=100

n= array(eval(input('n:')))
i=0
while(i < size(n)):
	if(n[i]==1):
		pts=pts+0
	elif(n[i]==2):
		pts=pts*2
	elif(n[i]==3):
		pts=pts/3
	elif(n[i]==4):
		pts=pts*4
	elif(n[i]==5):
		pts=pts/5
	elif(n[i]==6):
		pts=pts*6
	i=i+1
print (round(pts,2))
	
	