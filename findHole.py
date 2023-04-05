import numpy as np
import openpyxl
import pyperclip

def getSheet(xlsxFile='example.xlsx'):

    sheet = openpyxl.load_workbook(xlsxFile)['sheet1']  #获取一张表格（可能有多张表格）
    templist=[]
    allRows = [x for x in sheet.rows]          #获取所有行(cell对象）
    sheetSize = len(allRows)
    if sheetSize == (len(allRows[0])):             #检测行数与列数是否相等
        for i in range(len(allRows)):
            rowsValue = [x.value for x in allRows[i]]      #迭代一行里的每个cell,及其实际内容
            templist.append(rowsValue)                     #临时二维数组
        bb = np.rot90(np.array(templist),-1)      #与maya坐标匹配，对应x、y
        return bb, sheetSize
    else:
        print("This is not a squared sheet!!!!")

def findOne(sheet, size ):

    for i in range(size):
        for j in range(size):
            if sheet[i,j] == 0:
                startU, startV = i, j

                for ii in range(size-startU):
                    for jj in range(size-startV):
                        curU, curV = size-ii, size-jj
                        newa = np.array(sheet[startU:curU, startV:curV])
                        if np.sum(newa) == 0:
                            print('ggot it~~~~')
                            #print((startU, startV, curU, curV))
                            return startU, startV, curU, curV
def collecting_blocks(theList, size):
    blocks =[]
    findNs = size*size
    while findNs != 0:
        #print(findOne(aa))
        if findOne(theList, size):
            sU,sV,eU,eV = findOne(theList, size)
            blocks.append(list((sU,sV,eU,eV)))
            theList[sU:eU, sV:eV] = 1
        if np.sum(theList) == size*size:
            findNs = 0
        else:
            findNs -= 1

        print('qqq %d'%findNs)
    return blocks

sheet, sheetSize = getSheet()
if sheet.any():                         #判断是否有返回值
    getBB = collecting_blocks(sheet,sheetSize)
    pyperclip.copy(str(getBB))
