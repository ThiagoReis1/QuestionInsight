altura_joe = 1.77
taxa_joe = 0.02
l = float(input("altura: "))
t = float(input("taxa de crescimento: "))
anos=0
while l < altura_joe:
	altura_joe+=taxa_joe
	l+=t
	anos+=1
print(anos)