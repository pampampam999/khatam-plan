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

def Juz(inputJuz):
    return JUZ[inputJuz-1]

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
print("{} Hari lagi".format(resultDay.days))

#last read
lastRead = int(input("Last read (juz):"))
