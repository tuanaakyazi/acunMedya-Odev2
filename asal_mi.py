def asal_mi(sayi):
    asal = True
    if sayi < 2:
        asal = False
    for i in range(2,sayi//2 + 1):
        if sayi % i == 0:
             asal = False
             break
    return asal
def main():
    sayi = int(input("Lütfen bir sayi giriniz : "))
    if asal_mi(sayi):
        print("bu sayi asal.")
    else:
        print("bu sayi asal degil.")

if __name__== "__main__":
    main()
