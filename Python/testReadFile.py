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
        print('Số người trong folder là: ' + str(myList[i]))
    if (myList[i] > 0 and i == 1):
        print('Số xe máy trong folder là: ' + str(myList[i]))
    if (myList[i] > 0 and i == 2):
        print('Số xe đạp trong folder là: ' + str(myList[i]))
    if (myList[i] > 0 and i == 3):
        print('Số mặt người trong folder là: ' + str(myList[i]))
    if (myList[i] > 0 and i == 4):
        print('Số biển số ngắn trong folder là: ' + str(myList[i]))
    if (myList[i] > 0 and i == 5):
        print('Số biển số dài trong folder là: ' + str(myList[i]))
    if (myList[i] > 0 and i == 6):
        print('Số xe oto trong folder là: ' + str(myList[i]))
    if (myList[i] > 0 and i == 7):
        print('Số tải trong folder là: ' + str(myList[i]))
    if (myList[i] > 0 and i == 8):
        print('Số xe van trong folder là: ' + str(myList[i]))
    if (myList[i] > 0 and i == 9):
        print('Số xe bus trong folder là: ' + str(myList[i]))
    if (myList[i] > 0 and i == 10):
        print('Số bagac trong folder là: ' + str(myList[i]))
    if (myList[i] > 0 and i == 11):
        print('Số con chó trong folder là: ' + str(myList[i]))