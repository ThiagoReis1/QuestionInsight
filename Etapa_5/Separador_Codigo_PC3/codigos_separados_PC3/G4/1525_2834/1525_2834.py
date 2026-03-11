vo = int(input("volume inicial de agua: "))
vb = int(input("volume de agua bombeado: "))
vr = int(input("volume de agua retirado: "))

i = 0
a = 1000
v_m = (vo + vb) - vr

while(v_m > a):
	
	v_m = (vo + vb) - vr
	i = i - 1
	
print(i)