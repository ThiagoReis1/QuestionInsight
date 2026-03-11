import math
#
x = int(input(": "))


#
if x%19==0:
   f = x//19
   msg = "sim"

else :
	f = x%19
	msg = "nao"
#
print(f)
print(msg)
