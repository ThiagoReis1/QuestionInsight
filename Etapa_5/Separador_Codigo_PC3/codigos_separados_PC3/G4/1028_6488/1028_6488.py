v = float(input("Volume de agua consumida durante o mes: "))

# 100% - 1
# 35% - x
# 100x = 35
# x = 35/100 (:5)
# x = 7/20

f = (0.37 * v + 15) + (7/20) * (0.37 * v + 15)

print(round(f, 2))