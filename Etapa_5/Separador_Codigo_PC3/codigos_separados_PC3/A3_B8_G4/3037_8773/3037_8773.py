vx= float(input())
fx=0
if vx<=-1 or vx>=1: 
	fx= vx**2
elif (-1<vx<0) or (0<vx<1):
   fx= vx
elif vx==0:
	fx= 1
print(round(fx,4))
