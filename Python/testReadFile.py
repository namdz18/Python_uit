import os
import shutil

TongNguoi = 0
TongXeMay = 0
TongXeDap = 0
TongMatNguoi = 0
TongBienVuong = 0
TongBienDai = 0
TongOto = 0
TongXeTai = 0
TongVan = 0
TongBus = 0
TongBaGac = 0
TongDog = 0

dem = 0
path = '/Users/Admin/Desktop/Importantfolder/V3/5/'
files = os.listdir(path)
for file in files:
    fileNameExtentions = os.path.splitext(file)
    if fileNameExtentions[1] == '.txt':
        os.chdir('/Users/Admin/Desktop/Importantfolder/V3/5/')
        f = open(file, 'r')
        content = f.read()
        t = content.split()
        # print(t)
        demperson = 0
        demmotorbike = 0
        dembicycle = 0
        demface = 0
        demplate = 0
        demlongplate = 0
        demcar = 0
        demtruck = 0
        demvan = 0
        dembus = 0
        dembagac = 0
        demdog = 0
        for x in t:
            if x == '0':
                demperson = demperson + 1
            if x == '1':
                demmotorbike = demmotorbike + 1
            if x == '2':
                dembicycle = dembicycle + 1
            if x == '3':
                demface = demface + 1
            if x == '4':
                demplate = demplate + 1
            if x == '5':
                demlongplate = demlongplate + 1
            if x == '6':
                demcar = demcar + 1
            if x == '7':
                demtruck = demtruck + 1
            if x == '8':
                demvan = demvan + 1
            if x == '9':
                dembus = dembus + 1
            if x == '10':
                dembagac = dembagac + 1
            if x == '11':
                demdog = demdog + 1
        TongNguoi = TongNguoi + demperson
        TongXeMay = TongXeMay + demmotorbike
        TongXeDap = TongXeDap + dembicycle
        TongMatNguoi = TongMatNguoi + demface
        TongBienVuong = TongBienVuong + demplate
        TongBienDai = TongBienDai + demlongplate
        TongOto = TongOto + demcar
        TongXeTai = TongXeTai + demtruck
        TongVan = TongVan + demvan
        TongBus = TongBus + dembus
        TongBaGac = TongBaGac + dembagac
        TongDog = TongDog + demdog
        f.close()
myList = [TongNguoi, TongXeMay, TongXeDap, TongMatNguoi, TongBienVuong, TongBienDai, TongOto, TongXeTai, TongVan, TongBus, TongBaGac, TongDog]
for i in range (0, 11):
    if myList[i] == 0:
        continue
    if (myList[i] > 0 and i == 0):
        print('S??? ng?????i trong folder l??: ' + str(myList[i]))
    if (myList[i] > 0 and i == 1):
        print('S??? xe m??y trong folder l??: ' + str(myList[i]))
    if (myList[i] > 0 and i == 2):
        print('S??? xe ?????p trong folder l??: ' + str(myList[i]))
    if (myList[i] > 0 and i == 3):
        print('S??? m???t ng?????i trong folder l??: ' + str(myList[i]))
    if (myList[i] > 0 and i == 4):
        print('S??? bi???n s??? ng???n trong folder l??: ' + str(myList[i]))
    if (myList[i] > 0 and i == 5):
        print('S??? bi???n s??? d??i trong folder l??: ' + str(myList[i]))
    if (myList[i] > 0 and i == 6):
        print('S??? xe oto trong folder l??: ' + str(myList[i]))
    if (myList[i] > 0 and i == 7):
        print('S??? t???i trong folder l??: ' + str(myList[i]))
    if (myList[i] > 0 and i == 8):
        print('S??? xe van trong folder l??: ' + str(myList[i]))
    if (myList[i] > 0 and i == 9):
        print('S??? xe bus trong folder l??: ' + str(myList[i]))
    if (myList[i] > 0 and i == 10):
        print('S??? bagac trong folder l??: ' + str(myList[i]))
    if (myList[i] > 0 and i == 11):
        print('S??? con ch?? trong folder l??: ' + str(myList[i]))