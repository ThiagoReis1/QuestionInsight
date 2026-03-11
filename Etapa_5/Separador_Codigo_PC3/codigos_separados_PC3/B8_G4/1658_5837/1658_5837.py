from numpy import*
vet=input("Paises: ").split(',')
chn=0
jpn=0
kor=0
mgl=0
tha=0
vet2=zeros(5,dtype=int)
for i in range(size(vet)):
	if vet[i]=="CHN":
		chn=chn+1
		vet2[0]=chn
	elif vet[i]=="JPN":
		jpn=jpn+1
		vet2[1]=jpn
	elif vet[i]=="KOR":
		kor=kor+1
		vet2[2]=kor
	elif vet[i]=="MGL":
		mgl=mgl+1
		vet2[3]=mgl
	elif vet[i]=="THA":
		tha=tha+1
		vet2[4]=tha
print(max(vet2))
print(vet2)