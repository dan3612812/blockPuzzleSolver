from copy import deepcopy
from typing import List, Tuple
from .Puzzle import Puzzle
from colorama import Back

colorList = [Back.RED, Back.GREEN, Back.YELLOW,
             Back.BLUE, Back.MAGENTA, Back.CYAN, ]


class Map:
    def __init__(self, twoD: List[List[int]]) -> None:
        '''
        0 in map means empty can put puzzle
        -1 can't put in puzzle
        '''
        self.__fixedMap = deepcopy(twoD)
        self.__map = deepcopy(twoD)
        self.__mapX = len(twoD)
        self.__mapY = len(twoD[0])
        self.__puzzleId = 1
        self.__check()

    def __check(self):
        ySize = 0
        for x in self.__map:
            if ySize == 0:
                ySize = len(x)
            else:
                if ySize != len(x):
                    raise ValueError("the map format was error")

    def putInPuzzle(self, anchor: Tuple[int, int], puzzle: Puzzle) -> bool:
        # if the puzzle can put in the map then puzzleId +1
        # print("start put in, anchor",anchor)
        tempMap = deepcopy(self.__map)
        if puzzle.maxX()+anchor[0] > self.__mapX or puzzle.maxY()+anchor[1] > self.__mapY:
            # print("over size")
            return False
        for x in range(0, puzzle.maxX()):
            for y in range(0, puzzle.maxY()):
                point = puzzle.point(x, y)
                if point:
                    # the map'points is empty then can put the puzzle
                    np = tempMap[x+anchor[0]][y+anchor[1]]
                    if np == 0:
                        tempMap[x+anchor[0]][y+anchor[1]] = self.__puzzleId
                        continue
                    else:
                        return False
        self.__puzzleId += 1
        self.__map = tempMap
        return True

    def autoPutIn(self, puzzle: Puzzle) -> bool:
        for y in range(0, self.__mapY):
            for x in range(0, self.__mapX):
                if self.putInPuzzle((x, y), puzzle):
                    return True
        return False

    def draw(self):
        for x in self.__map:
            for y in x:
                point = y
                if point == 0:
                    print(Back.WHITE, "▢", Back.RESET, end="")
                elif point == -1:
                    print(Back.RESET, " ", Back.RESET, end="")
                else:
                    color = colorList[(point % len(colorList))-1]
                    print(color, point, Back.RESET, end="")
            print("")

    def clean(self):
        self.__puzzleId = 1
        self.__map = self.__fixedMap
    
    def bitwiseClockwiseRotate(self,):
        # TODO
        # [
        #  [1,0,0],
        #  [1,1,1]
        # ]
        # 2d covert to bit > 100 111
        # padding zero to puzzle max size =3 > 100 111 000
        # padding zero to map X size if X=5 > 10000 11100 00000
        # then clockwise rotate  11000 10000 10000
        # the formula is [(i mod X)-1]*5+nowPuzzleY-(i\X)

        None
    
    def covertToBit(self): 
        None