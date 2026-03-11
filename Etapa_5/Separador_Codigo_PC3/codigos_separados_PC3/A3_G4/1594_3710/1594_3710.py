from numpy import *

x = eval(input("Danos:"))

i=0;
j=0;
m=0;

while i<size(x):
	j = j + (i + 1) * x[i]
	i = i +1

print(j)