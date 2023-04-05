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

target = datetime.datetime(2023,4,24)
print(target.strftime("%d %m %Y"))
now = datetime.datetime.now()
print(now.strftime("%d %m %Y"))

result=target - now
print("{} Hari lagi".format(result.days))