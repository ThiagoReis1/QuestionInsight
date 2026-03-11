nmol = int(input())
vol = float(input())
temp = float(input())

r = 0.082057
t = temp + 273.1
p = (nmol*r*t )/vol
print(p)