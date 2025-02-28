def hesap_makinesi(sayi1, sayi2, islem):
    if islem == "+":
        sonuc = sayi1 + sayi2
        return (f"{sayi1} + {sayi2} = {sonuc}")
    elif islem == "-":
        sonuc  = sayi1 - sayi2
        return (f"{sayi1} - {sayi2} = {sonuc}")
    elif islem == "*":
        sonuc = sayi1 * sayi2
        return (f"{sayi1} * {sayi2} = {sonuc}")
    elif islem == "/":
        if sayi2 == 0:
            return "Hata: Bölme işlemi için ikinci sayi 0 olamaz!"
        sonuc = sayi1 / sayi2
        return (f"{sayi1} / {sayi2} = {sonuc}")
    else :
        return "Hata: Geçersiz işlem türü!"

def main():
    while True:
        sayi1 = float(input("Lütfen 1. sayiyi giriniz : "))
        sayi2 = float(input("Lütfen 2. sayiyi giriniz : "))
        islem = input("Lütfen yapmak istediginiz islemi giriniz (+, -. /, *) : ")
        sonuc =  hesap_makinesi(sayi1, sayi2, islem)
        print(f"{sonuc}")
        secim = input("devam etmek istiyor musunuz(E/H) : ")
        if secim == "E" or secim == "e":
            continue
        else:
            break
if __name__ == "__main__":
    main()