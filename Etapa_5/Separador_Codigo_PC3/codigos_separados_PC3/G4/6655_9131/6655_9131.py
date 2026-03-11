# 2 notas
from numpy import*
nts = array(eval(input("valor das notas")))
cred = [5, 1]
i = 0
nmd = 0
while (i < size(nts)):
   nmd = nmd + nts[i]*cred[i]
   i = i + 1
cf = nmd / sum(cred)
print(round(cf,2))
