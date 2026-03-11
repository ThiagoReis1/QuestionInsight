vr=float(input("velocidade:"))
seg=0
while(vr>=40):
	vr=vr-(vr*0.02)
	seg=seg+1
	
print(seg)