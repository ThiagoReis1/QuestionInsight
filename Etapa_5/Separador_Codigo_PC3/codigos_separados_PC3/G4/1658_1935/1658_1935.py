from numpy import*
tr=array(eval(input("<3   ")))
print(tr)
r=array(zeros(5),dtype(int))
a1="JPN"
a2="CHN"
a3="KOR"
a4="MGL"
a5="THA"
for e in tr:
	if(e==a1):r[0]=r[0]+1
	if(e==a2):r[1]=r[1]+1
	if(e==a3):r[2]=r[2]+1
	if(e==a4):r[3]=r[3]+1
	if(e==a5):r[4]=r[4]+1
print(r)