# import os,shutil
# targetPath = r"C:\Users\Administrator\Documents\Adobe\Adobe Substance 3D Painter\python\plugins"
# shutil.copy('OOP.py',targetPath)
mess=['aa.dfe','aa.uh','bb.se','bb.lll','cc.bb']
newl=[i for i in mess if any(ii.split('.')[0] == 'bb' for ii in mess) ]
print(newl)
#if any(name.split('.')[0] == 'bb' for  name in mess):
#    print(name)
result = next((item for item in mess if item.split('.')[0] == 'bb'), None)
print(result)