# file : ds2_osFileList.py 
# desc : 윈도우 파일 리스트

import os

fnameAry = []
folderName = 'C:/Windows/System32'

for dirName, subDirList, fnames in os.walk(folderName):
    for fname in fnames:
        fnameAry.append(fname)

print(len(fnameAry))
print(len(fnameAry))

fnameAry.sort(reverse=True)
print(fnameAry)