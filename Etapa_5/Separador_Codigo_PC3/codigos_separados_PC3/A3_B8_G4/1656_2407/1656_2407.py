from numpy import *
o = input("Origem: ")
v0 = zeros(5, dtype=int)

be = 0
es = 0 
fr = 0
it = 0
pt = 0
v1 = 0
o = o.split(",")
for i in o:
	if i == "BE":
		be = be + 1
	elif i == "ES":
		es = es + 1
	elif i == "FR":
		fr = fr + 1
	elif i == "IT":
		it = it + 1
	elif i == "PT":
		pt = pt + 1

		
v2 = array([be, es, fr, it, pt])
print(max(v2))
print(v2)