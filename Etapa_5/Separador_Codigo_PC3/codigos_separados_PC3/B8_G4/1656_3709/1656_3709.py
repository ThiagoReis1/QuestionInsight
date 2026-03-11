from numpy import*
v = input("v: ")
y = v.split(',')
x = zeros(5, dtype=int)
for i in y:
	if i.upper() == "BE":
		x[0] += 1
	elif i.upper() == "ES":
		x[1] += 1
	elif i.upper() == "FR":
		x[2] += 1
	elif i.upper() == "IT":
		x[3] += 1
	elif i.upper() == "PT":
		x[4] += 1
print(max(x))
print(x)