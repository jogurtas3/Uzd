'''#1 uzd
k =   int(  input("sk? ")  )
kk = k
for i in range(0,k) :
        print(kk)
        kk = kk*10+k

#2 uzd
a = int(input())
b=2*a
c=0
if a>1:
  e=1
else:
  e=0
f=0
h=a+1
for i in range (1, 2*a+1):
  b=b-1
  d=c
  c=a*(10**b)
  c=c+d
print(c)

for i in range (1, 2*a-2):
  f=e*10**(a-i)
  e=e*10+1

for i in range (1, a):
  g=e*10**i
  e=(e-11)//100
  c=c-g
  print(c)

for i in range (1, a+1):
  h=h-1
  g=e*10**h
  e=e*100+11
  c=c+g
  print(c)



#3 uzd
a = int(input())

for z in range(2, a+1):
        for y in range(1, z+1):
                for x in range (1, y+1):
                        print(y, end="")
                print()

a = int(input())

for z in range(2, a+1):
        for y in range(1, z+1):
                for x in range (1, 20-y):
                        print(" ", end="")
                for x in range (1, 2*y):
                        print(y, end="")
                print()

#4 uzd
nn = int(input())

for z in range(10):
        n=nn
        while(n>0):
                if n%10==z:
                        print(n%10, end="")
                n = n//10

n=nn
while(n>0):
        if n%10==9:
                print(n%10, end="")
        n = n//10



#5 uzd
n=int(input("kiek pazymiu? "))
sar = []
for i in range(1, n+1):
        p = int(input("iveskit " +str(i)+ "-aji pazymi "))
        sar.append(p)
        # saraso papildymas, nes sar dar neegzistuoja
print(sar)
vid = float(0)
for i in range(n):
        vid += sar[i]
# for p in sar:
#         vid += p
vid = vid / n
print(vid)

maz = sar[0]
for i in range(n):
        if sar[i]<maz:
                maz=sar[i]
print(maz)

didz = sar[0]
for i in range(n):
        if sar[i]>didz:
                didz=sar[i]
print(didz)



#6 uzd
nn = int(input("skaicius, kurio skaitmenys bus sudelioti didejancia tvarka: "))

for z in range(10):
        n=nn
        while(n>0):
                if n%10==z:
                        print(n%10, end="")
                n = n//10



#7 uzd
print()
sk=int(input())
m=[]
while sk>0:
        m.append(sk%10)
        sk = sk//10
# sk=input()
# m=list(sk)
m.sort()   
print(m)
m.reverse()
print(m)
for it in m:
        print(it, end="")

#7.5 uzd, nebaigta
print()
sk=int(input())
m=[0,0,0,0,0,0,0,0,0,0]
while sk>0:
        # m.append(sk%10)
        m[sk%10] =+ 1
        sk = sk//10
for i in range (10):
        for x in m:
                print(i*x)


#8 uzd
import math
a = int(input())
pirm = True
for i in range (2, int(math.sqrt(a)+1)):
        if a % i == 0:
                pirm = False
                break
if pirm :
        print("pirminis")
else :
        print("ne")


a = int(input("intervalo pradzia "))
b = int(input("intervalo pabaiga "))
m = []
n = []
for i in range(a, b+1):
        pirm = True
        for x in range (2, int(math.sqrt(i)+1)):
                if i % x == 0:
                        pirm = False
        if pirm and i != 1:
                m.append(i)
        else:
                n.append(i)

print("pirminiai skaiciai: ", m)
print("nepirminiai skaiciai: ", n)'''
