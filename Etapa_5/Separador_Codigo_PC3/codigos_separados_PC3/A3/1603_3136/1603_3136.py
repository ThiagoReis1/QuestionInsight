from numpy import*
v = array(eval(input("Vetor: ")))

anel1 = 80
anel2 = 40
anel3 = 20

c = 0

while(size(v) < 4):
	if(v[0] or v[1] or v[2] or v[3] == 1):
		c = c + 80
	print(c)