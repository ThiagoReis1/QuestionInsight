from numpy import*
n = array(eval(input("")))
pf = (n[0] + n[1] + n[2] + n[3]) - max(n) 
p1 = pf / 3.0
print(round(p1, 2))
if(p1>=5):
	x = "APROVOU"
else:
	x = "REPROVOU"
print(x)
