# a='python'
# b=317
# print('a:{}, b:{}')
# b,a = a,b

# for numer in range (1500,2701):
#     if numer %7==0 and numer % 5 ==0:
#         print(numer)

# def x():
#     print('hello word!')
#     print ('cos')

# def x():
#     return 3+3
# print(x())

# def s1(x, y):

# def fibbonaci_numbers (n)
#     ''' zwraca liczby fibonacciecio mniejsze od n '''
#     wynik =[]
#     a,b = 0,1
#         while len(wynik) < n:
#         wynik.append(a)
#         a, b = b, a + b
#     return wynik
# x= fibbonaci_numbers (10)

# def dlugosc (x):
#     a=0
#     for y in x:
#         a +=1
#     return a
#
# c= dlugosc('dlugosc')
# print(c)
#
# def sumalisty(l):
#     a=0
#     for i in l:
#         a=a+1
#     return a
#
# print(a([1,2,3,4,5]))


# Napisz funkcję w Pythonie, który mnoży wszystkie elementy na liście.

# def iloczyn(s):
#     a=s[0]
#     for i in s[1:]:
#         a*=i
#     return a
# v=iloczyn([99,88,77,66])
# print(v)

# Napisz funkcję w Pythonie, aby uzyskać największą liczbę z listy.

# def funkcja(r):
#     a=r[0]
#     for x in r[1:]:
#         if a<x:
#             a=x
#     return a
# b=[2,4,6,-8,5]
#
# c= funkcja(b)
# print(c)

# Napisz funkcję w Pythonie, który zlicza liczbę znaków (częstotliwość znaków) w ciągu tekstowym.
# Przykładowy ciąg tekstowy: google.com
# Oczekiwany wynik: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

# def zlicznie(t):
#     a={}
#     for x in t:
#         p=a.keys()
#         if x in p:
#             a[x]+=1
#         else:
#             a[x]=1
#     return a
# z=zlicznie('google.com')
# print(z)


# Napisz funkcję w Pythonie, który zlicza ciągi znaków, w których długość ciągu wynosi 2 lub więcej, a pierwszy i ostatni znak są takie same z podanej listy ciągów.
# Przykładowa lista : ['abc', 'xyz', 'aba', '1221']
# Oczekiwany wynik: 2

# def ciag (x):
#     licznik=0
#     for i in x:
#         if len(i) >=2 and i[:-1]==i[0]:
#             licznik+=1
#     return licznik
# print(ciag(['abc', 'xyz', 'aba', '1221']))

# Napisz funkcję w Pythonie, aby uzyskać listę posortowaną w porządku rosnącym według ostatniego elementu w każdej krotce z podanej listy niepustych krotek.
# Przykładowa lista: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Oczekiwany wynik : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# def fun1(krotka):
#     krotka[1]
#
# def sort(lista):
#     posrtowana = sorted(lista, key=fun1)
#     return posrtowana
# print(sort([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# s1='python'
#
# s2=s1[::-1]
#
# print(s2)

# lista= [1,'berta', 3, 4, -5,'kot,', -10.75, 3.14]
#
# print(lista[1:6])
#
# print(lista[2:6:2])
# print(lista[:4])

# lista = ["Rafal", "Agata", "Michal", "Pawel", "Grzegorz", "Robert", "A neta", "Tomasz", "Monika", "Klaudia", "Wiktor", "Kinga", "Marcin", "Tomasz", "Przemyslaw"]
# a= sorted (lista)
# print(a)
# print(len(a))
#
# tel = {'Maja': 500456, 'Jasio': 343455}
#
# print(tel)
#
# tel ['ola'] = 3024127
#
# print(tel)
#
# del tel['Maja']
#
# print(tel)
#
#  s1 = float(input('podaj pierwsza liczbę: '))
#  s2 = float(input('podaj druga liczbe: '))
#  s3 = s1/s2
#  s4 = s1%s2
#  s5 = s1//s2
#
#  print(s3,s4,s5)

# x=8
# y=15
#
# if x>3 or y%2==0:
#     print('Co najmniej jeden z warunków jest spełniony')
#
# if x<=3 or y%2!=0:
#     print('Żaden warunek nie jest spełniony')






