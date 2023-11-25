print("""**************************
Faktoriyel Bulma Programı

Programdan Çıkmak için 'q' ya basın

**************************
""")

while True:
    sayı = input("sayı:")
    if sayı == "q":
        print("Kapatılıyor...")
        break

    else:
        sayı = int(sayı)

        faktoriyel = 1

        for i in range(1,sayı+1):
            faktoriyel *= i
        print("{} sayısının faktöriyeli {}dır.".format(sayı,faktoriyel))

















