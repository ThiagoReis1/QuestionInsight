from numpy import*
n=array(eval(input("Informe a nota:")))
mn=n
s=size(n)-1
mf=(sum(n)-min(n))/s
print(round(mf, 2))
