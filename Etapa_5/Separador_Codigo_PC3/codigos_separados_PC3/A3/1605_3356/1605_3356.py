from numpy import *

a = array (eval(int(input())))

if (a == 1):
	anel1= a * 4
elif(a== 2):
	anel2 = a *2
elif(a== 3):
	anel3 = a
elif(a== 4):
	anel4 = a / 2
else:
	print("invalido")
print (round(anel1))
