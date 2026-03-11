n = int(input())

n1 = n // 100000
restn1 = n % 100000

n2 = restn1 // 10000
restn2 = restn1 % 10000

n3 = restn2 // 1000
restn3 = restn2 % 1000

n4 = restn3 // 100
restn4 = restn3 % 100

n5 = restn4 // 10
restn5 = restn4 % 10

n6 = restn5 // 1


t = n6
v = n1 + n2 + n3
z = n4 + n5 + n6

if(n == v - z **4 )


print(n1,n2,n3)



