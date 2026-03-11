from numpy import*
num = array(eval(input("num: ")))
i = int(input("num: "))
oc = 0
while oc < i:
	if num[0] == i:
		oc = oc+1
		print(0)
	if num[1] == i:
		oc = oc+1
		print(1)
	if num[2] == i:
		oc = oc + 1
		print(2)
	if num[3] == i:
		oc = oc + 1 
		print(3)
	if num[4] == i:
		oc = oc + 1 
		print(4)
	if num[5] == i: 
		oc = oc + 1 
		print(5)
print(oc - 1)
		
