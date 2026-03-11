da = float(input())
db = float(input())
ja = float(input())
jb = float(input())

t = 0
sa = da
sb = db

if((da>0) and (db>0) and (ja>0) and (jb>0) and (da>db) and (ja<jb)):
	while (sb < sa):
		sa = sa +(sa * (ja / 100))
		sa = round(sa, 2) 
		sb = sb +(sb * (jb / 100))
		sb = round(sb, 2)
		
		t = t + 1
	
else:
	t = "Dados incorretos"

print(t)	

		