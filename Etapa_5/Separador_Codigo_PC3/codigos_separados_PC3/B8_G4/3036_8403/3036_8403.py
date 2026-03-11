x = float(input())
if x <= -1 or x>= 1:
 fx = x
elif -1 <= x < 0 or 0 < x < 1:
 fx = 1
elif x == 0:
 fx = 2
print(round(fx,2))