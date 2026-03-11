from numpy import*

vet= input('vet:').split(',')
chn=0
jpn=0
kor=0
mgl=0
tha=0
for i in range(size(vet)):
	
	if(vet[i]=='CHN'):
		chn=chn+1
	elif(vet[i]=='JPN'):
		jpn=jpn+1
	elif(vet[i]=='KOR'):
		kor=kor+1
	elif(vet[i]=='MGL'):
		mgl=mgl+1
	elif(vet[i]=='THA'):
		tha=tha+1
		
v0 = array([chn,jpn,kor,mgl,tha])
print(max(v0))
print(v0)

	