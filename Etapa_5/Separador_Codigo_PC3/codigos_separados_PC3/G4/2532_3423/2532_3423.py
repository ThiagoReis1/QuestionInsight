c= input("c: ")
d= input("d: ")
m= input("m: ")
j= input("m: ")

r= c-((d+m)*j)
if (c>0) and (d>0) and (m>0) and (j>0):
	while (r <= c):
		tr= c/r 
	print(round(tr,2))
else:
	print("Dados incorretos")