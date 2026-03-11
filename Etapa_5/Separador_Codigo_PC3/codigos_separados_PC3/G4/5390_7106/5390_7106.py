from numpy import * 

c = input().upper()

e = c.count("A") + c.count("E") + c.count("I") + c.count("O") + c.count("U")
i = len(c) - e

v = e*0.19
con = i*0.23

total = v + con

print(round(total, 2))

	
