def penghitung_kata():
    while True:
        a = input('\nINPUT: ')
        b = a.split()
        aa = len(a)
        ##konfirmasi kebenaran jumlah karakter
        if aa != 6:
            #print("jumlah karkter tidak sesuai")
            aaa = 0
        else:
            #print("jumlah karakter oke")
            aaa = 1
        #konfirmasi kebenaran karakter 1
        bb = a[0]
        if bb == '0'or bb == '1'or bb == '2'or bb == '3' or bb == '4' or bb == '5' or bb == '6' or bb == '7' or bb == '8' or bb == '9' or bb == '10':
            #print("karakter pertama tidak oke")
            bbb = 0
        else:
            #print("karakter pertama oke")
            bbb = 1
        ##konfirmasi kebenaran karakter 2
        cc = a[1]
        if cc == 'a' or cc == 'i' or cc == 'u' or cc == 'e' or cc == 'o':
            #print("karekter kedua oke")
            ccc = 1
        else:
            #print("karakter kedua tidak oke")
            ccc = 0
        ##konfirmasi kebenaran karakter 3
        dd = a[2]
        if dd == 'c' or dd == 'b' or dd == 'D' or dd == 'F':
            #print("karakter ketiga tidak oke")
            ddd = 0
        else:
            #print("karakter ketiga oke")
            ddd = 1
        ##konfirmasi kebenaran karakter 4
        ee = a[3]
        if ee == ' ' or ee == '\n' or ee == '\r' or ee == '\t' or ee == '\f':
            #print("karakter empat tidak oke")
            eee = 0
        else:
            #print("karakter empat oke")
            eee = 1
        ##konfirmasi kebenaran karakter 5
        ff = a[4]
        if ff == 'A' or ff == 'I' or ff == 'E' or ff == 'U' or ff == 'O':
            #print("karakter lima oke")
            fff=1
        else:
            #print("karakter lima tidak oke")
            fff=0
        ##konfirmasi kebenaran karakter 6
        gg = a[5]
        if gg == ',' or gg == '.':
            #print("karakter enam tidak oke")
            ggg = 0
        else:
            #print("karakter enam oke")
            ggg = 1
        ##mengambil semua data nilai konfirmasi kebenaran
        if aaa == 1 and bbb == 1 and ccc == 1 and ddd == 1 and eee == 1 and fff == 1 and ggg == 1:
            print("\nOUTPUT : true")
        else:
            print("\nOUTPUT : false")
penghitung_kata()
