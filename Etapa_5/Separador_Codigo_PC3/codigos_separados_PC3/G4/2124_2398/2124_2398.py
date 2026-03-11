from numpy import*
nt = array(eval(input()))
sn = size(nt)
m = max(nt)
i = 0
while(i<sn):
	if(nt[i]==m):
		nt[i] = 0
		i = i+1
	else:
			i = i+1
mf = (nt[0]+nt[1]+nt[2]+nt[3])/3

print(round(mf, 2))
if (mf>=5):
	print("APROVOU")
else:
	print("REPROVOU")