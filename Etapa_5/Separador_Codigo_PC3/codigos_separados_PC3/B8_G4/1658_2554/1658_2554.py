from numpy import *
p=(input("paises: ")).split(',')
cont= zeros(5,dtype=int)
chn=0
jpn=0
kor=0
mgl=0
tha=0
for i in range(5):
	if(p[i]== 'CHN'):
		chn=chn+1
		cont[0]=cont[0] + chn
	elif(p[i]== 'JPN'):
		jpn=jpn+1
		cont[1]=cont[1] + jpn
	elif (p[i]=='KOR'):
		kor=kor+1
		cont[2]=cont[2] + kor
	elif(p[i]=='MGL'):
		mgl=mgl+1
		cont[3]=cont[3] + mgl
	elif(p[i]=='THA'):
		tha=tha+1
		cont[4]=cont[4] + tha
ta=max(cont)
print(ta)
print(cont)
	
		
		