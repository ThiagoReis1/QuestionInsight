from numpy import * 

v = input(': ').upper().split(',')


jpn = 0
chn = 0
mgl = 0
tha = 0
kor = 0
g = []
for i in v:
	if (i == "JPN"):
		jpn = jpn + 1
	elif ( i == 'CHN'):
		chn = chn + 1
	elif ( i ==  'MGL'):
		mgl = mgl + 1
	elif ( i == 'THA'):
		tha = tha + 1
	elif ( i == 'KOR'):
		kor = kor + 1
		
g.append(chn)
g.append(jpn)
g.append(mgl)
g.append(tha)
g.append(kor)

m = max(g)
print(m)
print(g)		


		