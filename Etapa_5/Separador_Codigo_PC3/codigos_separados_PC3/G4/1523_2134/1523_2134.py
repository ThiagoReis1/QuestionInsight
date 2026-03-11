from math import*

a=int(input("digite:"))
b=int(input("digite:"))
c=int(input("digite:"))


d=a
total=0

while(d<200):
	d=(d+b)-c
	total=total+1

print(total)

