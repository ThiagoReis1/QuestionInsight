from numpy import*

n = array(eval(input()))
m = max(n)
s =n[0]+n[1]+n[2]+n[3]-max(n)
st = (s/3)
print(round(st,2))

if(st>=5.0):
	print("APROVOU")
else:
	print("REPROVOU")