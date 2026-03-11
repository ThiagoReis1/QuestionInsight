from math import *

qi = int(input("qi For.:"))
qi2 = int(input("qi Lok.:"))
pa = float(input("pa For.:"))
pa2 = float(input("pa Lok.:"))

u=0
i=0
s=0

while(qi2<qi):
		qi=qi+(qi*pa)/100
		qi2=qi2+(qi2*pa2)/100
		s=s+1

print(s)