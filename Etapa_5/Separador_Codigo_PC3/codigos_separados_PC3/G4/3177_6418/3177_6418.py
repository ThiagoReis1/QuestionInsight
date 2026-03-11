from numpy import *

A = str(input())
a=0
for i in A:
	if i == ("a" or "A"):
		a = a + 1
print("a: "+str(a))

e=0
for i in A:
	if i == ("e" or "E"):
		e+=1
print("e: "+ str(e))

i=0
for k in A:
	if k == ("i" or "I"):
		i+=1
print("i: "+ str(i))

o=0
for i in A:
	if i == ("o" or "O"):
		o+=1
print("o: "+ str(o))

u=0
for i in A:
	if i == ("u" or "U"):
		u+=1
print("u: "+str(u))