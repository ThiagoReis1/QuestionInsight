a = float(input())
from math import *
if(a<=0):
	print("0")
elif(0<a<=1):
	print("1")
elif(1<a<=2):
	print(round(sqrt(a),4))
elif(a>2):
	b = a**(1/3)
	print(round(b,4))