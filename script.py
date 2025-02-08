while True:
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    secim = input("Bir işlem seçin: ")

    if secim == "1":
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        print("Sonuç:", sayi1 + sayi2)
    elif secim == "2":
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        print("Sonuç:", sayi1 - sayi2)
    elif secim == "3":
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        print("Sonuç:", sayi1 * sayi2)
    elif secim == "4":
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        print("Sonuç:", sayi1 / sayi2)



