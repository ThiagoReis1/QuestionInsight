from numpy import *
v = eval(input())
x = 0
y = 0

for i in v:
	if i > 170:
		x += i 
		y += 1
		media = x/y

if y == 0:
	media = 0.0
	
print(round(media,2))