from numpy import*
hgh = array(eval(input(":")), dtype=float)
m = hgh[0]
f = hgh[1]*2
c = hgh[2]*3
gdf = (m+ f+c)/6
print(round(gdf, 2))