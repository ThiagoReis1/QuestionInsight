x = float(input())
k = int(input())

i = 0
s = 0

while (i < k):
	s = s + x/(2*i + 1)
	i = i + 1
if(i == k):
	print(round(s,8))
