def no2():
    while True:
        ary = []
        a = input("masukan kalimat = ")
        d = {}
        for c in a:
            ary.append(c)
            lset = set()
            [(lset.add(item), ary.append(item)) for item in ary if item not in lset]
            stra = ""
        print (stra.join(lset))
no2()
