m= 7.25
p= 4.75
r= 3.50

c= input().upper()

i= 0
t= 0

while i  < len(c):
	if c[i] == "M":
		t= t + m
	elif c[i] == "P":
		t= t + p
	elif c[i] == "R":
		t= t + r
	i = i + 1
print(t)