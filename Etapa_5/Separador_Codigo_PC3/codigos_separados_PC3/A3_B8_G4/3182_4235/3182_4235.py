from numpy import*
vet = array(eval(input()))
p = zeros(10,dtype=int)
for i in range(0,9,-3):
	if(i==0):
		p[0]=p[0]+1
	elif(i==1):
		p[1]= p[1]+1
	elif(i==2):
		p[2]= p[2]+1
	elif(i==2):
		p[3]= p[3]+1
	elif(i==3):
		p[4]= p[4]+1
	elif(i==4):
		p[5]=p[5]+1
	elif(i==5):
		p[6]= p[6]+1
	elif(i==6):
		p[7]=p[7]+1
	elif(i==7):
		p[8] = p[8]+1
	elif(i==8):
		p[9]=p[9]+1
	elif(i==9):
		p[10]= p[10]+1
print(p)
