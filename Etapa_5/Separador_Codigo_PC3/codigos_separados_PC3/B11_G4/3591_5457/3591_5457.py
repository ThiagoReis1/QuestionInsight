from numpy import *

num = array(eval(input("digite o numero: ")))
i = 0
pont = 0

while i < size(num):
	if num[i] == 1: 
		pont = pont + 10
	if num[i] == 2:
		pont = pont + 5
	if num[i] == 3:
		pont = pont + 10
	if num[i] == 4:
		pont = pont + 5
	if num[i] == 5:
		pont = pont + 10
	if num[i] == 6:
		pont = pont + 5
	i = i + 1
	
print(pont)