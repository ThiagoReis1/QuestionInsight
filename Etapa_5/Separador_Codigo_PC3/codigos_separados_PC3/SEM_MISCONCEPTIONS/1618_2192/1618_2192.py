from numpy import *

c = array(eval(input()))

t = size(c)

s = []
i = 0


while(i < t):
	if(i == 0):
		s = c[0]
	elif(i == 1):
		s = str(c[1]^x) + " + " + C[0]
	elif(i == 2):
		s = str(c[2]^2) + " + " + str(c[1]^x) + " + " + C[0]
	elif(i == 3):
		s = srt(c[3]^3 + " + " + str(c[2]^2) + " + " + str(c[1]^x) + " + " + C[0]
	elif(i == 4):
		s = srt(c[4]^4 + " + " + srt(c[3]^3 + " + " + str(c[2]^2) + " + " + str(c[1]^x) + " + " + C[0]
	i = i + 1 

print(s)