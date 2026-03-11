from numpy import*
vn = array(eval(input()))
vg = array(eval(input()))
n = size(vn)
i=0
s1=0
s2=0
s3=0
s4=0
s5=0
while(i<n):
	if(vn[i]=="BANANA"):
		s1=vg[i]*0.97
	elif(vn[i]=="BIFE"):
		s2=vg[i]*2.95
	elif(vn[i]=="FEIJOADA"):
		s3=vg[i]*1.27
	elif(vn[i]=="OMELETE"):
		s4=vg[i]*1.04
	elif(vn[i]=="TOMATE"):
		s5=vg[i]*0.2
	i=i+1
st=s1+s2+s3+s4+s5
print(round(st,2))