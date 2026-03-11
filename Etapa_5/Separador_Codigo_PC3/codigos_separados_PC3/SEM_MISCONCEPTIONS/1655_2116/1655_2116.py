from math import*
x = input().split(',')
ac=0
am=0
pa=0
ro=0
rr=0
for i in x:
	if(i == "AC"):
   ac = ac + 1
	elif(i == "AM"):
   am = am + 1	
	elif(i == "PA"):
   pa = pa + 1	
	elif(i == "RO"):
   ro = ro + 1	
	elif(i == "RR"):
   rr = rr  + 1
print(max(x))
print(array(soma))