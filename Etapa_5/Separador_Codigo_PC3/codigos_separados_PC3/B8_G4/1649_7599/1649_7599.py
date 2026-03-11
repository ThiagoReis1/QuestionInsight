from numpy import * 
cor = input("cor de olhos:").upper().split(',')
v0 = zeros(5,dtype=int)
for i in cor:
	if(i=="P"):
		v0[0] = v0[0] + 1
	elif(i=="C"):
		v0[1] = v0[1] + 1
	elif(i=="M"):
		v0[2] = v0[2] + 1
	elif(i=="V"):
		v0[3] = v0[3] + 1
	elif(i=="A"):
		v0[4] = v0[4] + 1
print(max(v0))
print(v0)
	
	
	

