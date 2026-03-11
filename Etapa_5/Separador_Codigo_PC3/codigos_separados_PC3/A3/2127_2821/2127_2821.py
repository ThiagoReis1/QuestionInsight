from numpy import*
from numpy.linalg import*
v = array(eval(input("")))
for i in range(size(v)):
	if(v[0]==min(v)):
		MEDIA = (v[1]+v[2]+v[3])/3
	if(v[1]==min(v)):
		MEDIA = (v[0]+v[2]+v[3])/3
	if(v[2]==min(v)):
		MEDIA = (v[0]+v[1]+v[3])/3
	if(v[3]==min(v)):
		MEDIA = (v[0]+v[1]+v[2])/3
print(round(MEDIA,2))
if(MEDIA>=50.0):
	print("APROVADO")
else:
	print("REPROVADO")
		
		
