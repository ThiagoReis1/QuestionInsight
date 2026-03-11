from numpy import*
s=input("Digite os países: ").split(",")

chn=0
jpn=0
kor=0
mgl=0
tha=0
for i in s:
	if(i=="CHN"):
		chn=chn+1
	elif(i=="JPN"):
		jpn=jpn+1
	elif(i=="KOR"):
		kor=kor+1
	elif(i=="MGL"):
		mgl=mgl+1
	elif(i=="THA"):
		tha=tha+1
v=array([chn,jpn,kor,mgl,tha])
print(max(v))
print(v)