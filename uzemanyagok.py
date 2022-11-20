class Adatok:
    def __init__(self , list):
        self.date = list[0]
        self.y = int(list[0].split(".")[0])
        self.m = int(list[0].split(".")[1])
        self.d = int(list[0].split(".")[2])
        self.benzin = int(list[1])
        self.eu_benzin = round(int(list[1])/307.7, 2)
        self.gazolaj = int(list[2])
        self.eu_gazolaj = round(int(list[2])/307.7, 2)
        self.kulonbseg = abs(self.benzin-self.gazolaj)

def importFromTXT():
    list = []
    f = open("uzemanyag.txt" , "r" , encoding="utf8").read()
    lines = f.split("\n")
    for i in range(len(lines)):
        list.append(Adatok(lines[i].split(";")))
    return list

def feladat4(list):
    temp_id = 0
    for i in range(len(list)):
        if list[i].kulonbseg < list[temp_id].kulonbseg:
            temp_id = i
    return list[temp_id].kulonbseg

def feladat5(list, num):
    temp = 0
    for i in list:
        if i.kulonbseg == num:
            temp += 1
    return temp

def feladat6(list):
    for i in list:
        if i.y%4 == 0 and i.m == 2 and i.d == 24:
            return f"Volt"
    return "Nem volt"

def feladat7(list):
    f = open("euro.txt", "w", encoding="UTF8")
    for i in list:
        f.write(f"{i.date};{i.eu_benzin};{i.eu_gazolaj}\n")
    f.close()

def feladat8():
    while True:
        temp = input("8. feladat: Kérem adja meg az évszámot [2011..2016]")
        if 2011 < int(temp) < 2016:
            return int(temp)

def feladat9(o1, o2):
    dateMap = dict()
    if o1.y%4 == 0:
        list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(1, len(list)+1):
            dateMap[i] = list[i-1]
    else:
        list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(1, len(list)+1):
            dateMap[i] = list[i-1]

    if o1.m == o2.m:
        return abs(o1.d - o2.d)
    else:
        temp1 = dateMap[o1.m] - o1.d
        return temp1 + o2.d

def feladat10(list, num):
    temp_list = []
    temp = 0
    for i in range(len(list)):
        if list[i].y == num:
            temp_list.append(list[i])
    for i in range(1, len(temp_list)):
        if feladat9(temp_list[i-1], temp_list[i]) > temp:
            temp = feladat9(temp_list[i-1], temp_list[i])
    return temp





def main():
    main_list = importFromTXT()
    print(f"3. feladat: Változások száma: {len(main_list)}")
    print(f"4. feladat: A legkisebb különbség: {feladat4(main_list)}")
    print(f"5. feladat: A legkisebb különbség előfordulása: {feladat5(main_list, feladat4(main_list))}")
    print(f"6. feladat: {feladat6(main_list)} változás szökőnapon!")
    feladat7(main_list)
    user_inp_y = feladat8()
    print(f"10. feladat: {user_inp_y} évben a leghosszabb időszak {feladat10(main_list, user_inp_y)}")
main()