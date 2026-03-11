from numpy import*

v = array(eval(input("Digite: ")))
i = 0
s = 10000
while(i < size(v)):
	if(v[i] == 1):
		s = (s * 1)
	elif(v[i] == 2):
		s = s 
	if(v[i] == 3):
		s = s / 2
	if(v[i] == 4):
		s = s / 4
	i = i + 1
print(round(s, 2))
		
		