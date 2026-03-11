snowtotal=float(input())
saistotal=float(input())
amanitatotal=float(input())

snow=snowtotal/0.31
sais=saistotal/0.73
amanita=amanitatotal/2.64

x=min(snow,sais,amanita)
print(int(x))