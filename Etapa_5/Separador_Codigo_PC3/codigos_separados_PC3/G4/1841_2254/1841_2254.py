q_0 = float(input("valor_0:"))
rend = float(input("rendimento:"))
from math import *
anos = ((log(3 * q_0) - log(q_0))/rend)
print(int(anos + 1))