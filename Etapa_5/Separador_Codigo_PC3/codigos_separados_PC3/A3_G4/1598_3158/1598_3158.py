from numpy import*

a = array(eval(input("")))
b = 0
s = 0
total = []

for i in range(size(a)):
	if(i>=80):
		b = i*0.5
		
print(round(sum(a),2))