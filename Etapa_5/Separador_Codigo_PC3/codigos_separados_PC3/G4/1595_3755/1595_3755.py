from numpy import *
n=array(eval(input('Quais foram as notas:')))
x=min(n)
l=size(n)
s=sum(n)
m=(s-x)/(l-1)
print(round(m,2))