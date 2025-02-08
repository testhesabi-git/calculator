while True:
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Kare Al")

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
    elif secim == "5":
        sayi1 = float(input("Sayı girin: "))
        print("Sonuç", sayi1 * sayi1)
    else:
        print("Lütfen geçerli bir seçim yapın.(1-4)")



