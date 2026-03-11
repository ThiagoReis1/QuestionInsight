from numpy import*
a = input("pais: ").split(",")
t = zeros(5,dtype=int)
be = 0
es = 0
fr = 0
it = 0
pt = 0
for i in  a:
	if (i == "BE"):
		be = be + 1
	elif (i == "ES"):
		es = es + 1
	elif (i == "FR"):
		fr = fr + 1
	elif (i == "IT"):
		it = it + 1
	elif (i == "PT"):
		pt = pt + 1	
t[0]= be
t[1]= es
t[2]= fr
t[3]= it
t[4]= pt

print(max(t))
print(t)