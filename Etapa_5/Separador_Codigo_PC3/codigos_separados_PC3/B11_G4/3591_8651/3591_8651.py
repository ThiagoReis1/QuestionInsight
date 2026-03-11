from numpy import *

a = array(eval(input("face do dado: ")))

pont = 0
i = 0
while i < size(a):
	if a[i] == 1:
		pont = pont + 10
	if a[i] == 2:
		pont = pont + 5
	if a[i] == 3:
		pont = pont + 10
	if a[i] == 4:
		pont = pont + 5
	if a[i] == 5:
		pont = pont + 10
	if a[i] == 6:
		pont = pont + 5
	i = i + 1
print(pont)