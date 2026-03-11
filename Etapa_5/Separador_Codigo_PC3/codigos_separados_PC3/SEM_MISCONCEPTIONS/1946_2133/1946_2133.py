f=input("digite o nome")

o=15.9994
c=12.011
n=14.0067
s=32.066
h=1.0079

contaf=(c*9)+(h*11)+(o*2)+(s*2)
contat=(c*9)+(h*11)+(n*3)+(o*3)
if(f.lower=="fenilalanina""):
  print(round(contaf,2))
else:
  print(round(contat,2))