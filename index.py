while True:
    print("menghitung apa hari ini?")
    print("1.persegi")
    print("2. persegi panjang")
    print("3. segitiga")
    print("4. trapesium")
    print("5. lingkaran")
    print("6.Exit")
    
    pilihan = input("Pilih (1-6): ")
    #kita bikin rumus dulu
    def calculate_segitiga(alas, tinggi):
        segitiga = alas * tinggi / 2
        return segitiga
    
    def calculate_persegi(sisi):
        persegi = sisi * sisi
        return persegi
    
    def calculate_persegipanjang(panjang, lebar):
        persegipanjang = panjang * lebar
        return persegipanjang
    
    def calculate_trapesium(a, b, tinggi):
        trapesium = a + b * tinggi / 2
        return trapesium
    
    def calculate_lingkaran(r):
        lingkaran = r * r * 3.14
        return lingkaran
    
    if pilihan == "1":
        print(" ")
        sisi = int(input("sisi = "))
        print(calculate_persegi(sisi))
        print(" ")
        
    elif pilihan == "2":
            print(" ")
            panjang = int(input("panjang = "))
            lebar = int(input("lebar = "))
            print(calculate_persegipanjang(panjang, lebar))
            print(" ")
