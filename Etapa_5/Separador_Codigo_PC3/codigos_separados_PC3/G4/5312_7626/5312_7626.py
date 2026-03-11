ba= int(input(""))
t= int(input(""))

c= 0
while c != t:
	r= int(ba* 0.02)
	ba= (ba+ r)
	c= c+1
print(int(ba))