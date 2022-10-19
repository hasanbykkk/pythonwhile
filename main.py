# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

giriş="1-toplama" \
      "2-çıkarma" \
      "3-çarpma" \
      "4-bölme" \
      "5-karesini hesaplama" \
      "6-karekökünü alma"
print(giriş)
anahtar =1


while anahtar==1:
    soru=input("yapmak istediğiniz işlemin numarasını girin")
    if soru=="Q":
        print("çıkılıyor")
        anahtar=0
    elif soru=="1":
        say1 =int(input("toplamak istediğiniz sayıyı giriniz"))
        say2 = int(input("toplamak istediğiniz sayıyı giriniz"))
        print(say1,"+",say2,"cevap" , say1+say2 ,)
    elif soru=="2":
        sayı3=int(input("çıkarmak için birinci yazın"))
        sayı4=int(input("çıkarmak için ikinci sayı yazın "))
        print(sayı3,"-",sayı4,"=",sayı3-sayı4)
    elif soru=="3":
        sayı5=int(input("çarpmak istediğiniz birinci sayı"))
        sayı6=int(input("çarpmak istediğiniz ikinci sayı"))
        print(sayı5, "*", sayı6, "=", sayı5 * sayı6)
    elif soru=="4":
        sayı7=int(input("böleceğiniz sayıyı yazınız"))
        sayı8=int(input("bölecek sayıyı giriniz"))
        print(sayı7,"/",sayı8,"=",sayı7/sayı8)
    elif soru=="5":
        sayı9=int(input("Karesini hesaplamak istediğiniz sayıyı girin"))

        print(sayı9,"sayının karekökü",sayı9**2)
    elif soru=="6":
        sayı10=float(input("karekökünü alcagınız sayıyı giriniz="))
        print(sayı10,"sayının karekökü",sayı10**0,5)
    else:
        print("yanlış sayı girdiniz ")
        print("burdaki seçeneklerden giriniz",giriş,)


