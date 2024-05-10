# mesaj: KRIPTOGRAFI
mesaj="0100101101010010010010010101000001010100010011110100011101010010010000010100011001001001"

# n ve e değerini kendi seçtğimiz q ve p değerlerinden elde edebiliriz.
n=252953
e=7 


# eğer imza eklemek isterseniz, aşağıdaki satırlarıda aktif hale getirebilirsiniz.
# imza = "100100001011"
# mesaj = mesaj + imza.zfill(24)

#mesaj bloğunu 2 bytelık parçalara bölüyorum
bloklar = [mesaj[i:i+16] for i in range(0, len(mesaj), 16)] 
print(bloklar)
sifreli_bloklar = ""
bin_bloklar = ""
for blok in bloklar:
    blok_int = int(blok, 2)
    sifreli_blok = pow(blok_int, e, n)
    sifreli_blok_str = str(sifreli_blok)
    sifreli_bloklar += " "+sifreli_blok_str
    bin_bloklar += " "+bin(int(sifreli_blok_str))[2:].zfill(24)
print("Şifreli bloklar:", sifreli_bloklar)
print("Şifreli binary bloklar:", bin_bloklar)
