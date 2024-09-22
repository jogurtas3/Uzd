m = [1, 5, 6, 1, 6,]
h = [4, 9]
# print(m[len(m)-1])
# m.append(1)

# m.insert(2, 2)
# m[0] = 3
# print(m)
# m.extend(h)
# print(m)
# print(9 in m)
# m.remove(1)
# m.pop(3)
# print(m)

# for skaicius in m:
#     print(skaicius)

# for index in range(len(m)):
#     print(index)

# print("////////////////")
# for index in range(len(m)-1, -1, -2):
#     # if index != 0 and index != 1:
#     print(m[index])

# n = list("8954")
# for sk in n:
#     value = int(sk)
#     print(type(sk), type(value))

# for i in range (m.count(1)):
#         m.remove(1)
# print(m)

# while 1 in m:
#     m.remove(1)
# print(m)

# a = int(input())
# aa = a
# for i in range (a):
#     print(aa)
#     aa = aa*10+a

# a = int(input())
# b = a*2
# c = a
# e = 1
# for i in range(b-1):
#     c = c*10+a
# print(c)

# for i in range(b-3):
#     e = e*10+1

# f = e
# for i in range(1, a):
#     f = e * (10 ** i)
#     c = c - f
#     e = (e - 11)//100
#     print(c, f)

# for i in range (a):
#     e = e * 100 + 11
#     f = f // (10 ** i)
#     print(c, e, f)
#     c = c + f

# a = int(input())
# b = 2 * a
# maxx = b - 1
# vid = (b - 1) // 2
# for i in range (b):
#     for j in range(b):
#         if i > vid:
#             i = maxx - i
#         if j > vid:
#             j = maxx - j          
#         if i < j:
#             print(a-i, end = "")
#         if j < i:
#             print(a-j, end = "")
#         if i == j:
#             print(a-i, end = "")
#     print()

# a = int(input())
# b = 2 * a
# maxx = b - 1
# vid = maxx // 2
# for i in range (b):
#     for j in range (b):
#         if i < vid:
#             i = vid - i
#         if j < vid:
#             j = vid - j
#         if i < j:
#             print(a - i, end = "")
#         if j < i:
#             print(a - j, end = "")
#         if i == j:
#             print(a - i, end = "")
#     print()

# a = int(input())

# for k in range (a - 1):
#     for i in range (k + 2):
#         for j in range (i + 1):
#             print(i + 1, end = "")
#         print()

# a = int(input())
# b = " "

# for k in range(a - 1):
#     for j in range (k + 2):
#         print(b * (a - (j + 1)), end = "")
#         for i in range (j + 1 + j):
#             print(j + 1, end = "")
#         print()

# a = int(input())
# b = a
# c = 0
# m = []
# while b > 0:
#     c += 1
#     b = b // 10

# b = a
# for i in range(c):
#     m.append(b % 10)
#     b = b // 10
# print(m)
# m.sort()
# print(m)
# for j in range(0, len(m)):
#     print(m[j], end = "")

#1 uzd
# d = int(input())
# s = int(input())
# r = int(input())
# g = int(input())
# k = g / (d + s +r)
# print("k = " + str(round(k, 2)))

# v1 = 8
# m1 = 29
# m2 = 43
# v = 9
# m = 5
# vnauja = 0
# mnauja = 0
# if m1 + m2 >= 60:
#     vnauja = v1 + 1
#     mnauja = m1 + m2 - 60
# else:
#     mnauja = m1 + m2
#     vnauja = v1
# print(vnauja, mnauja)
# if vnauja < v:
#     print("Petras i pamoka nepaveluos")
# elif vnauja == v and mnauja <= m:
#     print("Petras i pamoka nepaveluos")
# else:
#     print("Petras i pamoka paveluos")

# kelias = 320
# k = 20
# t = 100
# d = 2
# v = 10
# n = 4
# b = 10
# pinigu = k * t
# deg_kaina = n * (kelias / 100) * b
# isnaudos = d * v * k + deg_kaina
# if pinigu >= isnaudos:
#     print("gali")
# else:
#     print("negali")

# n = int(input())
# m = int(input())
# t_visas = 0
# for i in range(n):
#     t = int(input())
#     t_visas += t
# v = round(m * n / t_visas, 1)
# print("Sportininko vid greitis v = " + str(v) + "m/s, distancijoje sugaiso " + str(t_visas) + " sekundes.")

# t1 = 17
# k = 3
# t = 65
# n = 0
# t_visas = 0
# while t_visas < t:
#     t1 += k
#     t_visas += t1
#     n += 1
#     print (t1, t_visas, n)
# print("Mama pagamins " + str(n) + " patiekalus.")

# isvis_zuvu = int(input())
# dideliu = 0
# skaniu = 0
# parsinese = 0
# svoris_isvis = 0
# svoris = 1
# ar_skani = 1
# while True:
#     dar = input("Ar dar yra zuveliu? ")
#     if dar == "N":
#         break
#     svoris = float(input())
#     ar_skani = int(input())
#     if svoris >= 1:
#         dideliu += 1
#     if ar_skani == 1:
#         skaniu += 1
#     if svoris >= 1 and ar_skani == 1:
#         parsinese += 1
#         svoris_isvis += svoris
# print (parsinese, svoris_isvis)
# print(dideliu, skaniu)

# p_isvis = 0
# with open("papildomai.txt", "r") as file:
#     n = int(file.readline())
#     for i in range(n):
#         p = float(file.readline())
#         p_isvis += p
# with open("rezultatas.txt", "w") as file:
#     file.write(format(p_isvis, '.2f'))


# isvis = 0
# with open("papildomai.txt", "r") as file:
#     eilute = (file.readline().split(" "))
#     k = int(eilute[0])
#     m = int(eilute[1])
#     n = int(eilute[2])
#     for i in range(n):
#         isvis += k
#         k += m
# with open("rezultatas.txt", "w") as file:
#     file.write(str(isvis))

# t_isvis = 0
# with open("papildomai.txt", "r") as file:
#     n = int(file.readline())
#     for i in range(n):
#         t = int(file.readline())
#         t_isvis += t
# vid = t_isvis / n
# with open("rezultatas.txt", "w") as file:
#     file.write(str(t_isvis))
#     file.write("\n")
#     file.write(str(vid))

# t_isvis = 0
# with open("papildomai.txt", "r") as file:
#     eilute = file.readline().split()
#     n = int(eilute[0])
#     x = int(eilute[1])
#     b = int(eilute[2])
#     for i in range(n):
#         line = file.readline().split()
#         t = int(line[0])
#         k = int(line[1])
#         t_isvis += t + ((x - k) * b)
#         print(t, k, t_isvis)
# with open("rezultatas.txt", "w") as file:
#     file.write(str(t_isvis))