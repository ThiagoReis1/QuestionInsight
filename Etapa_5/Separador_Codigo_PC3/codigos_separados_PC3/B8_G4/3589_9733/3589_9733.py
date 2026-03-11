from numpy import*
n = array(eval(input("po:")))
i = 0
s = 0
com = size(n)
while i < com:
	if n[i] == 1:
		s = s+80
	elif n[i] == 2:
		s = s+40
	if n[i] == 3:
		s = s+20
	elif n[i] == 4:
		s = s+10
	i = i+1
	
print(s)






