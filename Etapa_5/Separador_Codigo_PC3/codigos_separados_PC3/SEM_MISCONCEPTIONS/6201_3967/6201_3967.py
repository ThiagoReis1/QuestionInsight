a_joe = 1.77
t_joe = 0.02

a_qq = float(input())
t_qq = float(input())

i = 0

while a_qq < a_joe:
	a_joe = a_joe + t_joe
	a_qq = a_qq + t_qq
	i = i + 1
	
print(i)