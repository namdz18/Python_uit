import os

dem = 0
path = '/Users/Admin/Desktop/Importantfolder/V3/5/'
files = os.listdir(path)
for file in files:
    fileNameExtentions = os.path.splitext(file)
    if fileNameExtentions[1] == '.jpg':
        dem += 1;
print(f'Số lượng ảnh trong một folder là: {dem}')