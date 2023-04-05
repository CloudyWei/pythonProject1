from typing import List, Union
numList = List[Union[int, float]]

def ccSum(alist: numList) -> Union[int, float]:
     ret = 0
     for a in alist:
          ret += a
     return ret
al = [1,2,3,4,5,6]
fl = [0.1,0.2,0.3,0.4,0.5,0.6,5,6]
print(ccSum(fl))
p = eval(input('godd:'))
match p:
     case (0):
          print('good 0')
          