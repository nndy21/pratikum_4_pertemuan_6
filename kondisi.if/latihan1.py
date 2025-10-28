a = int(input("Masukan bilangan pertama: "))
b = int(input("Masukan bilangan kedua: "))
c = int(input("Masukan bilangan ketiga: "))
d = int(input("Masukan bilangan keempat: "))

if a > b and a > c and a > d:
    terbesar = a
elif b > a and b > c and b > d:
    terbesar = b
elif c > a and c > b and c > d:
    terbesar = c
else:
    terbesar = d


print("Bilangan terbesar adalah:", terbesar)
