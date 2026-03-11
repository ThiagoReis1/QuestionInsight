n = int(input("populacao inicial:"))
ta = float(input("taxa anual de crescimento:"))
r = int(input("numero de tracajas roubados:"))

t = ta/100
i = 0
s = 0
while(n>0):
 s = n + (n*t)
 n = s - (500 + r)
 i = i + 1
print(i)