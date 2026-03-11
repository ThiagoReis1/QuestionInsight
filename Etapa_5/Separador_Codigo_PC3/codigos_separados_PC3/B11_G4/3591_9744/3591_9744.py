from numpy import*
v = array(eval(input()))
a = 0
b = 0
while(a<size(v)):
	if(v[a]== 1):
		b+=10
	if(v[a] == 2):
		b+=5
	if(v[a] == 3):
		b+= 10
	if(v[a] == 4):
		b+= 5
	if(v[a] == 5):
		b+= 10
	if(v[a] == 6):
		b+= 5
	a+=1
print(int(b))