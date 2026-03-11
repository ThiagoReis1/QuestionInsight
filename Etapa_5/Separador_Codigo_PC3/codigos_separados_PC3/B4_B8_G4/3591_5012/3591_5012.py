from numpy import*
d = eval(input("dados: "))

i =0 
c=0

while(i < size(d)):
	if(d[i] == 1):
		t = 10
	elif(d[i] == 2):
		t = 5
	elif(d[i] == 3):
		t =10
	elif(d[i] == 4):
		t = 5
	elif(d[i] == 5):
		t = 10 
	elif(d[i] == 6):
		t = 5
	c = c + t
	i = i + 1
print(c)