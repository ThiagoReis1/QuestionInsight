from numpy import*

d = array(eval(input("dados: ")))
i = 0
p = 0

while(i<size(d)):
	if(d[i] == 1):
		p = p + 10
	elif(d[i] == 2):
		p = p + 5
	elif(d[i] == 3):
		p = p + 0
	elif(d[i] == 4):
		p = p + 5
	elif(d[i] == 5):
		p = p + 20
	elif(d[i] == 6):
		p = p + 10
		
	i = i + 1
		
print(p)
		