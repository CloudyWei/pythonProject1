import openpyxl
import os
'''
 A and B column :texture--->mats dictionary
 C column: target ; D column: output result
'''

def getMatByTex(texList=[]):
    files = os.listdir(os.getcwd())
    xlslF = [a for a in files if a.endswith('.xlsx')][0]     # find xlsx file
    texMatDict={}
    table = openpyxl.load_workbook(xlslF)
    sheet = table["sheet1"]
    for tex in sheet['A']:   # setup dictionary:tex('A'column)--mat('B'column)
        texMatDict.setdefault(tex.value, sheet['B{}'.format(tex.row)].value)
    newbook=openpyxl.Workbook()
    newSheet=newbook.active
    for tex in sheet['C']:              # get tex searching mat for
        texList.append(tex.value)
    texList=texList[1:]              # ignore fisrt row
    for t in texList:
        print(mat :=texMatDict.setdefault(t, 'unknowMat')) #;print(mat)
        newSheet.append({'D':mat,})
        #print(texMatDict[t])
    newbook.save('{}'.format(xlslF.replace('.xlsx', '_new.xlsx')))

getMatByTex()
