cpm= 0.37
f= 15

v= float(input("Volume de agua consumida durante o mes: "))

tm1= (v*0.37)+15
tm2= (tm1*35)/100
tf= tm1+tm2

print(round(tf, 2))
