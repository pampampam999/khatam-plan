import datetime

################################################################
#                   github.com/pampampam999                    #
################################################################

class Alquran:
    #Constanta
    TOTALAYATALQURAN = 6236 #Jumlah total ayat alquran yang di pakai
    JUZ = [
        148,
        111,
        126,
        131,
        124,
        110,
        149,
        142,
        159,
        127,
        151,
        170,
        154,
        227,
        185,
        269,
        190,
        202,
        339,
        171,
        178,
        169,
        357,
        175,
        246,
        195,
        399,
        137,
        431,
        564,
    ]
    SURAH = [
    7, 
    286,
    200,
    176,
    120,
    165,
    206,
    75,
    129,
    109,
    123,
    111,
    43,
    52,
    99,
    128,
    111,
    110,
    98,
    135,
    112,
    78,
    118,
    64,
    77,
    227,
    93,
    88,
    69,
    60,
    34,
    30,
    73,
    54,
    45,
    83,
    182,
    88,
    75,
    85,
    54,
    53,
    89,
    59,
    37,
    35,
    38,
    29,
    18,
    45,
    60,
    49,
    62,
    55,
    78,
    96,
    29,
    22,
    24,
    13,
    14,
    11,
    11,
    18,
    12,
    12,
    30,
    52,
    52,
    44,
    28,
    28,
    20,
    56,
    40,
    31,
    50,
    40,
    46,
    42,
    29,
    19,
    36,
    25,
    22,
    17,
    19,
    26,
    30,
    20,
    15,
    21,
    11,
    8,
    8,
    19,
    5,
    8,
    8,
    11,
    11,
    8,
    3,
    9,
    5,
    4,
    7,
    3,
    6,
    3,
    5,
    4,
    5,
    6,

]
    BOBOTPERJUS=1000 #Setiap Juz di berikan Bobot sama rata , untuk menentukan score per ayat

    BOBOT = list() #Variable bobot per ayat pada Juz tersebut
    for i in range(30): #Perhitungan dan memasukkan BOBOT per ayat 
        temp=BOBOTPERJUS/JUZ[i]
        BOBOT.append(temp)
        #print(i,BOBOT[i])

user = Alquran()



########################################################################
#Function
########################################################################
def cekJuz(InputTotalAyat):
    hasilJuz = 1
    tempJuz = 0
    if InputTotalAyat == 0:
        pass
    else:
        for i in range(31):
            if InputTotalAyat <= tempJuz:
                #print("{} kurang dari {}".format(InputTotalAyat,tempJuz))
                hasilJuz = i
                #print("Juz ke",i)
                break
            else:
                tempJuz += JUZ[i]    
        
    return hasilJuz


#input target
inputTargetDay = int(input("Target Khatam (D) :"))
inputTargetMon = int(input("Target Khatam (M) :"))
inputTargetYear = int(input("Target Khatam (Y) :"))
#print(inputTargetDay,inputTargetMon,inputTargetYear)

targetKhatam = datetime.datetime(inputTargetYear,inputTargetMon,inputTargetDay)
print(targetKhatam.strftime("%d %m %Y"))

#input start date
inputStartDay = int(input("Start Read (D) :"))
inputStartMon = int(input("Start Read (M) :"))
inputStartYear = int(input("Start Read (Y) :"))
#print(inputStartDay,inputStartMon,inputStartYear)

#now = datetime.datetime.now()
startDate = datetime.datetime(inputStartYear,inputStartMon,inputStartDay)
#print(now.strftime("%d %m %Y"))
print(startDate.strftime("%d %m %Y"))

#calcuating days left
resultDay=targetKhatam - startDate
hariMenujuKhatam = resultDay.days
# hariMenujuKhatam = 16 #manual input , don't forget to coment
print("{} Hari lagi".format(hariMenujuKhatam))

#input last read
lastReadAyat = int(input("Last Read (ayat):")) # ayat ke 2
lastReadSurah = int(input("Last Read (surah):")) #surah ke 2

#calculating total surah has read
#Get total ayat in surah has read
totalAyat = 0

if lastReadSurah == 0:
    pass
else:
    for i in range(lastReadSurah-1):
        #print(i, SURAH[i])
        totalAyat += SURAH[i]
        #print("Total",totalAyat)

# jumlah nya di tambah dengan ayat terakhir
totalAyat += lastReadAyat
print("Total ayat : ",totalAyat)


#cek sekarang juz brp
sekarangJuz=cekJuz(totalAyat)


#kurang berapa ayat sampai selesai
totalKurangAyat =  TOTALAYATALQURAN - totalAyat
print("Kurang ayat : ",totalKurangAyat)


#mencari kurang brp ayat di juz itu
temp= totalAyat #temp untuk menghitung ayat pada juz itu

for i in range(cekJuz(totalAyat) - 1):
    temp -= JUZ[i]
    #print("Temp di kurangi dengan Juz {} yaitu sebanyak {} ayat, sehingga {}".format(cekJuz(totalAyat)-1,JUZ[i],temp))
totalKurangAyatDiJuzItu=JUZ[cekJuz(totalAyat)-1]-temp
juzSelanjutnya=cekJuz(totalAyat)+1
if juzSelanjutnya == 31:
    print("Kurang {} ayat untuk menuju Juz {}".format(totalKurangAyatDiJuzItu,"Khatam"))
else:
    print("Kurang {} ayat untuk menuju {}".format(totalKurangAyatDiJuzItu,juzSelanjutnya))
sekian = 1- (temp / JUZ[cekJuz(totalAyat)-1]) 


#cek kurang brp juz
print("Sekarang Juz :",cekJuz(totalAyat))
totalKurangJuz = 30 - sekarangJuz
print("Detail Kurang Juz :",totalKurangJuz + sekian)

#cek kurang bobot menuju akhir dari kurang brp ayat menuju akhir
kurangBobot=( totalKurangJuz * BOBOTPERJUS)+(totalKurangAyatDiJuzItu * BOBOT[sekarangJuz-1])
print("Total Kurang Bobot",kurangBobot)
bobotHarian = kurangBobot / hariMenujuKhatam#int(resultDay.days)  #ubah hari left di sini
print("Bobot Harian :",bobotHarian)


#mencari sampai ayat berapa harus membaca
tempHitungAyat = totalAyat
tempBobotHarian = bobotHarian
tempStatusLoop = 1
# i=0
# while i<10:
#     print(i)
#     i+=1

for i in range(hariMenujuKhatam):
    while tempStatusLoop:

        #jika sudah ayat 6236 maka tidak perlu mengecek ayat selanjutnya
        if tempHitungAyat == TOTALAYATALQURAN: 
            break    

        #cek bobot ayat selanjutnya
        # print("Temp hitung ayat sebelum di cek ayat selanjutnya",tempHitungAyat)
        bobotAyatSelanjutnya=BOBOT[cekJuz(tempHitungAyat +1)-1]
        #print("Bobot Ayat Selanjutnya", bobotAyatSelanjutnya)


        #print("Bobot harian sebelum",tempBobotHarian)
        if tempBobotHarian- bobotAyatSelanjutnya >0: #jika ayat selanjutnya dapat di baca dengan score bobot sekarang
            #print("Bobot harian {} jika di kurang bobot selanjutnya {}, hasilnya masih positif".format(tempBobotHarian,bobotAyatSelanjutnya))
            tempBobotHarian-=bobotAyatSelanjutnya
            #print("Bobot harian setelah di kurangi",tempBobotHarian)
            tempHitungAyat+=1
            #print("Total Ayat menjadi",tempHitungAyat)
            #print("")
            
        else: #jika temp bobot harian habis ( point kurang untuk membeli ayat selanjutnya)
            #karena berhenti di 6235 (kurang1  ayat) maka menambahkan score biar selesai perhitungan
            if tempHitungAyat == 6235:
                #print("karena 6235 maka temp ++")
                #tempHitungAyat += 1
                # print("Temp bobot harian sekarang:",tempBobotHarian)
                tempBobotHarian+= bobotAyatSelanjutnya*2
                # print("Temp bobot harian sesudah di tambah:",tempBobotHarian)
            else:
                tempStatusLoop=False   
                tempBobotHarian += bobotHarian
                    

            

            # print("Bobot harian sebelum {} di tambah bobot harian hari berikutnya {}".format(tempBobotHarian-bobotHarian,tempBobotHarian))
    
    print("Hari ke {} sampai ayat ke {}".format(i+1,tempHitungAyat))
    tempStatusLoop = 1

# for i,bobot in enumerate(BOBOT):
#     print(i,bobot,bobot*JUZ[i])
        




