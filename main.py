import datetime

#Data 
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

def cekJuz(InputTotalAyat):
    hasilJuz = 1
    tempJuz = 0
    for i in range(31):
        if InputTotalAyat <= tempJuz:
            #print("{} kurang dari {}".format(InputTotalAyat,tempJuz))
            hasilJuz = i
            #print("Juz ke",i)
            break
        else:
            tempJuz += JUZ[i]    
        
    return hasilJuz
    

# #input target
# inputTargetDay = int(input("Target Khatam (D) :"))
# inputTargetMon = int(input("Target Khatam (M) :"))
# inputTargetYear = int(input("Target Khatam (Y) :"))
# #print(inputTargetDay,inputTargetMon,inputTargetYear)

# targetKhatam = datetime.datetime(inputTargetYear,inputTargetMon,inputTargetDay)
# print(targetKhatam.strftime("%d %m %Y"))

# #input start date
# inputStartDay = int(input("Start Read (D) :"))
# inputStartMon = int(input("Start Read (M) :"))
# inputStartYear = int(input("Start Read (Y) :"))
# #print(inputStartDay,inputStartMon,inputStartYear)

# #now = datetime.datetime.now()
# startDate = datetime.datetime(inputStartYear,inputStartMon,inputStartDay)
# #print(now.strftime("%d %m %Y"))
# print(startDate.strftime("%d %m %Y"))

# #calcuating days left
# resultDay=targetKhatam - startDate
# print("{} Hari lagi".format(resultDay.days))

#input last read
lastReadAyat = int(input("Last Read (ayat):")) # ayat ke 2
lastReadSurah = int(input("Last Read (surah):")) #surah ke 2

#calculating total surah has read
#Get total ayat in surah has read
totalAyat = 0
for i in range(lastReadSurah-1):
    #print(i, SURAH[i])
    totalAyat += SURAH[i]
    #print("Total",totalAyat)

# jumlah nya di tambah dengan ayat terakhir
totalAyat += lastReadAyat
print("Total ayat : ",totalAyat)

print(cekJuz(totalAyat))



