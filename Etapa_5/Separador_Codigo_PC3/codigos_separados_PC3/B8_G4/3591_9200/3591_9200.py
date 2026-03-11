from numpy import*

n = array(eval(input("digite: ")))
i = 0
t = 0

while(i < size(n)):
	if(n[i] == 1):
		f1 =10
		t = t + f1
	elif(n[i] == 2):
		f2 = 5
		t = t + f2
	elif(n[i] == 3):
		f3 = 10
		t = t + f3
	elif(n[i] == 4):
		f4 = 5
		t = t + f4
	elif(n[i] == 5):
		f5 = 10
		t = t + f5
	elif(n[i] == 6):
		f6 = 5
		t = t + f6
	i = i + 1
	
print(t)
		