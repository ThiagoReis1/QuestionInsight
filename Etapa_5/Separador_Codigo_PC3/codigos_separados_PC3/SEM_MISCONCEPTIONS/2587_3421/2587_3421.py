from numpy import*

velt= array(eval(input("VETOR: ")))

l=vet[0]
ls= l+(*0.60)
n=0
for i in range(size(vet)):
   if (vet[i]>ls):
      print(i)
      n=n+1
   
print(n)
