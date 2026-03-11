from numpy import *
media= array(eval(input("nota:")))

a = sum(media)
b = max(media)
c= a-b
d = c/3.0


print(round(d,2))

if(d >= 5.0):
	print("aprovou".upper())
else:
	print("reprovou".upper())