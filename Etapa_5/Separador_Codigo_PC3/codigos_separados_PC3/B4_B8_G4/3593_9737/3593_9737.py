from numpy import*

vt = array(eval(input()))
tam = size(vt)
pts = 200

i = 0
while i < tam:
	if vt[i] == 1:
		pts = pts / 2
	elif vt[i] == 2:
		pts = pts * 3
	elif vt[i] == 3:
		pts = pts / 2
	elif vt[i] == 4:
		pts = pts * 3
	elif vt[i] == 5:
		pts = pts / 2
	elif vt[i] == 6:
		pts = pts * 3
	i += 1
print(round(pts,2))