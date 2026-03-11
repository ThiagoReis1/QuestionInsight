from numpy import*

n = array(eval(input('')))

i = 0
pts = 100

while i < size(n):
	if n[i] == 1:
		pts = pts * 5
	elif n[i] == 2:
		pts = pts * 3
	elif n[i] == 4:
		pts = pts / 2
	i += 1
	
print(round(pts,2))
