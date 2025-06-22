"""
x = input('1.sayı: ') #inout kullanıcıdan veri alır
y = input('2.sayı: ')

print(type(x)) # veri tipini gösterir
print(type(y))

toplam = int(x) + int(y)  # input ile alınan veriler string olarak gelir, bu yüzden int() ile dönüştürülür

print(toplam)
"""
"""
x = 5               #int
y = 2.5             #float
name = 'Çınar'      #str
isOnline = True     #bool

# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isOnline))

# Type Conversion

# int to float

# x = float(x)
# print(x)
# print(type(x))

# float to int

# y = int(y)
# print(y)
# print(type(y))

# result = str(x) + str(y)
# print(result)
# print(type(result))

# bool to str

# isOnline = str(isOnline)
# print(isOnline)
# print(type(isOnline))

# bool to int

isOnline = False

isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))
"""
"""
pi = 3.14

r = float(input("yarı çap: "))

alan = pi * (r ** 2)
print(type(alan))

cevre = 2 * pi * r
print(type(cevre))

print("alan: "+ str(alan) + " çevre: "+ str(cevre))
"""
"""
name = 'Sadık'
surname = 'Turan'
age = 36

greeting = 'My name is '+ name + ' '+ surname + ' and \nI am '+ str(age) + ' years old'  
length = len(greeting)  # greeting'in uzunluğunu alır

# print(greeting)              # greeting'i ekrana yazdırır
# print(greeting[0])           
# print(greeting[3])
# print(greeting[length-1])   # son karakteri ekrana yazdırır
# print(greeting[-1])
# print(greeting[3:7])        #  # 3. indeksten 7. indekse kadar olan karakterleri ekrana yazdırır
# print(greeting[3:])
# print(greeting[:16])           
print(greeting[2:40:3])       # # 2. indeksten başlayarak 40. indekse kadar 3'er atlayarak karakterleri ekrana yazdırır
"""
name = 'Çınar'
surname = 'Turan'
age = 36

# print('My name is {} {}'.format(name, surname))               # bosluğa isim ve soyisim yazdırır  
# print('My name is {1} {0}'.format(name, surname))             
# print('My name is {s} {n}'.format(n=name, s=surname))        
# print("My name is {} {} and I'm {} years old.".format(name, surname, age))
# print("My name is {} {} and I'm {} years old.".format(name, name, name))

# result = 200 / 700
# print('the result is {r:1.4}'.format(r=result))     #1 solda kac bosluk olacagı, 4 ise ondalık basamak sayısı

print(f"My name is {name} {surname} and I'm {age} years old.")