# n sayda Fibonacci ədədini çap edən proqram
n = int(input("Fibonacci ədədlərin sayını daxil edin: "))

a, b = 0, 1
if n <= 0:
    print("Daxil edilmiş say mənfi ola bilməz!")
elif n == 1:
    print("Fibonacci ədədi= ", a)
else:
    fibonacci_sayisi = [a, b]
    for i in range(2, n):
        axirinci_eded = a + b
        fibonacci_sayisi.append(axirinci_eded)
        a, b = b, axirinci_eded
    print("Fibonacci ədədləri= ", fibonacci_sayisi)
