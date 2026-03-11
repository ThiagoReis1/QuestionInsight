from numpy import*
vt=array(eval(input("Tempo: ")))
vp=array(eval(input("Percentual:")))
i=0
p=0
while(i<size(vp)):
	p+=(vp[i]*5/100)*vt[i]
	i=i+1
print(round(p,2))