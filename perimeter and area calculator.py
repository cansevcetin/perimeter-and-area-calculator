pi = 3.14

while(True):
    print("""Sekil Cevre-Alan Hesaplayiciya Hosgeldiniz
         Hesaplama Yapilabilen Sekiller:
         Kare
         Dikdotrgen
         Ucgen
         Daire
         PRogramdan cikmak icin 'q' giriniz. """)
    sekil = input("Lutfen bir sekil seciniz:")
    if(sekil == "q"):
        print("Program Kapatiliyor...")
        break
    elif(sekil == "kare" or sekil == "Kare"):
        while(True):
            print("Hesaplama sekilleri:\n"
                  "1-)Cevre\n"
                  "2-)Alan")
            hesaplama_turu = input("Lutfen hesaplama turunu giriniz:")
            if(hesaplama_turu == "1"):
                kare_kenar = int(input("Lutfen karenin bir kenarini giriniz:"))
                cevre = kare_kenar*4
                print("Karenin cevresi :",cevre)
                break
            elif(hesaplama_turu == "2"):
                kare_kenar = int(input("Lutfen karenin bir kenarini giriniz:"))
                alan = kare_kenar*kare_kenar
                print("Karenin alani :",alan)
                break
            else:
                print("Eksik ya da hatali tuslama.")
    elif(sekil == "dikdortgen" or sekil == "Dikdortgen"):
        while(True):
            print("Hesaplama sekilleri:\n"
                  "1-)Cevre\n"
                  "2-)Alan")
            hesaplama_turu = input("Lutfen hesaplama turunu giriniz:")
            if(hesaplama_turu == "1"):
                dikdortgen_kenar1 = int(input("Lutfen dikdorgenin kisa kenarini giriniz:"))
                dikdortgen_kenar2 = int(input("Lutfen dikdorgenin uzun kenarini giriniz:"))
                cevre = (dikdortgen_kenar1+dikdortgen_kenar2)*2
                print("Dikdortgenin cevresi :",cevre)
                break
            elif(hesaplama_turu == "2"):
                dikdortgen_kenar1 = int(input("Lutfen dikdorgenin kisa kenarini giriniz:"))
                dikdortgen_kenar2 = int(input("Lutfen dikdorgenin uzun kenarini giriniz:"))
                alan = dikdortgen_kenar1*dikdortgen_kenar2
                print("Dikdortgenin alani :",alan)
                break
            else:
                print("Eksik ve ya hatali tuslama")
    elif(sekil == "ucgen" or sekil == "Ucgen"):
        while(True):
            print("Hesaplama sekilleri:\n"
                  "1-)Cevre\n"
                  "2-)Alan")
            hesaplama_turu = input("Lutfen hesaplama turunu giriniz:")
            if(hesaplama_turu == "1"):
                ucgen_kenar1 = int(input("Lutfen ucgenin birinci kenarini giriniz:"))
                ucgen_kenar2 = int(input("Lutfen ucgenin ikinci kenarini giriniz:"))
                ucgen_kenar3 = int(input("Lutfen ucgenin ikinci kenarini giriniz:"))
                if(ucgen_kenar1 == ucgen_kenar2 or ucgen_kenar1 == ucgen_kenar3 or ucgen_kenar2== ucgen_kenar3):
                    print("Girdiginiz ucgen ikizkenardir.")
                elif(ucgen_kenar1 == ucgen_kenar2 == ucgen_kenar3):
                    print("Girdiginiz ucgen eskenardir.")
                cevre = ucgen_kenar1+ucgen_kenar2+ucgen_kenar3
                print("Ucgenin cevresi :",cevre)
                break
            elif(hesaplama_turu == "2"):
                ucgen_kenar1 = int(input("Lutfen ucgenin birinci kenarini giriniz:"))
                ucgen_kenar2 = int(input("Lutfen ucgenin ikinci kenarini giriniz:"))
                ucgen_kenar3 = int(input("Lutfen ucgenin ikinci kenarini giriniz:"))
                if (ucgen_kenar1 == ucgen_kenar2 or ucgen_kenar1 == ucgen_kenar3 or ucgen_kenar2 == ucgen_kenar3):
                        print("Girdiginiz ucgen ikizkenardir.")
                elif (ucgen_kenar1 == ucgen_kenar2 == ucgen_kenar3):
                        print("Girdiginiz ucgen eskenardir.")
                u = (ucgen_kenar1+ucgen_kenar2+ucgen_kenar3)/2
                alan = (u*(u-ucgen_kenar1)*(u-ucgen_kenar2)*(u-ucgen_kenar3))**(1/2)
                print("Girdiginiz ucgenin alani :",alan)
                break
            else:
                print("Eksik ve ya hatali tuslama")
    elif(sekil == "daire" or sekil == "Daire"):
        while(True):
            print("Hesaplama sekilleri:\n"
                              "1-)Cevre\n"
                              "2-)Alan")
            hesaplama_turu = input("Lutfen hesaplama turunu giriniz:")
            if(hesaplama_turu == "1"):
                cap = int(input("Lutfen dairenin capini giriniz:"))
                cevre = 2*pi*(cap/2)
                print("Dairenin cevresi :",cevre)
                break
            elif(hesaplama_turu == "2"):
                cap = int(input("Lutfen dairenin capini giriniz:"))
                alan = pi*((cap/2)*(cap/2))
                print("Dairenin alani :",alan)
                break
            else:
                print("Eksik ve ya hatali tuslama")
    else:
        print("Lutfen dogru sekil seciniz.")