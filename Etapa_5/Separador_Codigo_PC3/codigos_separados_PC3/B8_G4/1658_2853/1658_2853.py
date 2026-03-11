from numpy import *

s = input("Insira algo: ").upper().split(',')
chn = 0
jpn = 0
kor = 0
mgl = 0
tha = 0

for i in s:
	if(i == 'CHN'):
		chn += 1
	elif(i == 'JPN'):
		jpn += 1
	elif(i == 'KOR'):
		kor += 1
	elif(i == 'MGL'):
		mgl += 1
	elif(i == 'THA'):
		tha += 1
print(max(chn,jpn,kor,mgl,tha))

v = zeros(5, dtype=int)
v[0] = chn
v[1] = jpn
v[2] = kor
v[3] = mgl
v[4] = tha
print(v)