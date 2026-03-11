
#
t = 3.50
s = 5.00
a = 13.00
#
x = input(": ")
q = int(input("y:"))
z = int(input("z:"))
#
if x == "T":
	f = (q*t) + (z*a)
else :
	f = (q*s) + (z*a)
#
print(round(f,2))


