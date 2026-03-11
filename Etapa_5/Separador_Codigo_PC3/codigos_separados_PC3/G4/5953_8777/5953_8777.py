p = 13.50
l = 6.00
r = 3.00
a = input("lanche ou p.e:")
q1 = int(input())
if q1 == p:
   q1*p
else:
	q1*l
q2 = int(input())*r

pf1 = q1*p*q2
pf2 = q1*l*q2
if a == pf1:
   print(round(pf1, 2))
else:
	print(round(pf2, 2))