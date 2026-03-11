ven = float(input())

if(ven<=1000):
	print(round(ven*0.05,2))	
else:
	cam1 = 1000*0.05
	cam2 = (ven - 1000)*0.1
	print(round(cam1+cam2,2))