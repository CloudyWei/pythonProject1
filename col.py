# -*- coding:utf-8 -*-
import os
import copy
import openpyxl
os.getcwd()
class ColGenerater(object):
    def __init__(self, *args, **kwargs):
        self.tableData = [[1, 1, 1, 0, 1],
                          [1, 0, 1, 1, 1],
                          [1, 1, 1, 1, 1],
                          [1, 1, 1, 0, 1],
                          [1, 1, 1, 1, 1]]
        self.colBlock = []

    def do(self):
        table = self.tableData
        block_start= [0,0]
        block_end = [0,0]
        for u in range(3):

            for v in range(3):

                if table[u][v] == 1:               #mark the start point
                    block_start[0] += u
                    block_start[1] += v
                    canMove = True                #True until find the endpoint
                    canTurnRight, canTurnUp = True, True
                    block_end[0] += block_start[0]
                    block_end[1] += block_start[1]

                    while canMove:

                        if (table[block_end[0]+1][block_end[1]] + table[block_end[0]][block_end[1]+1] + table[block_end[0]+1][block_end[1]+1]) == 3:    #mark the end point,
                            block_end[0] += 1                                    #quartic moving at this time
                            block_end[1] += 1
                            table[block_end[0] + 1][block_end[1]] = 0
                            table[block_end[0]][block_end[1] + 1] = 0
                            table[block_end[0] + 1][block_end[1] + 1] = 0
                            print('move quar-')
                            print(block_end)

                        elif (table[block_end[0]][block_end[1]+1]) == 1 and not self.isUTypeTCross(self.tableData, u, v) and canTurnRight==True:  #moving at u
                            block_end[0] += 1
                            canTurnUp = False
                            table[block_end[0]][block_end[1]+ 1] = 0
                            print('move right-----')
                            print(block_end)
                        elif (table[block_end[0]][block_end[1]+1]) == 1 and not self.isVTypeTCross(self.tableData, u, v) and canTurnUp == True:  #moving at v
                            block_end[1] += 1
                            canTurnRight =False
                            table[block_end[0]][block_end[1] + 1] = 0
                            print('move up->')
                            print(block_end)

                        else:
                            canMove = False
                            #block_end[0] += 0
                            #block_end[1] += 0
                        if block_end[0] > 3 or block_end[1] > 4:
                            canMove = False
                    self.colBlock.append(copy.deepcopy(block_end))
                    block_end[0] = 0
                    block_end[1] = 0
                    block_start[0] =0
                    block_start[1] =0

        return self.colBlock
                
    def isUTypeTCross(self, table, u, v):
        if (table[u-1][v] + table[u+1][v]) == 0 and (table[u-1][v+1] + table[u+1][v+1]) == 2:

            return True
    def isVTypeTCross(self, table, u, v):
        if (table[u][v-1] + table[u][v+1]) == 0 and (table[u+1][v+1] + table[u+1][v-1]) == 2:
            return True


col_b = ColGenerater()
allccs = col_b.do()
for cc in allccs:
    print(cc)




