n = int(input())
a = n//100000
ra = n%100000
b = ra//10000
rb = ra%10000
c = rb//1000
rc = rb%1000
d = rc//100
rd = rc%100
e = rd//10
re = rd%10
f = re
x = a+b+c
y = d+e+f
if (n == (x-y))