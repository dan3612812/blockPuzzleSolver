from typing import List


class Puzzle:
    def __init__(self, twoDArray: List[List[bool]]) -> None:
        '''
        [
            [1,0,1],
            [0,1,1],
            [1,0,0],
        ]
        '''
        self.__twoD = twoDArray
        # self.solidSquare = False
        self.__check()
        self.__binary = None

    @property.getter
    def binary(self):
        return 

    def covertToBinary(self):
        n = 0b1
        for y in self.__twoD:
            for i in y:
                n = n << 1
                n = n | i

        None

    def __check(self):
        ySize = 0
        for x in self.__twoD:
            if ySize == 0:
                ySize = len(x)
            else:
                if ySize != len(x):
                    raise ValueError("the map format was error")

    def isSolidSquare(self):
        #  TODO
        # don't need rotate ,because will same
        #  all points is 1 and x and y is equal
        #  if puzzle is cross also don't need rotate
        return None

    def __createRotate2D(self):
        new2D = [[None]*self.maxX() for i in range(self.maxY())]
        return new2D

    @property
    def twoD(self) -> List[List[int]]:
        return self.__twoD

    def clockwiseRotate(self,):
        '''
        The new 2d size is [max(oldY),max(oldX)]
        The new 2d rules is 
        newX=oldY
        newY=maxX-oldX
        '''
        new2D = self.__createRotate2D()
        for x in range(self.maxX()):
            for y in range(self.maxY()):
                newX = y
                newY = self.maxX()-x-1
                new2D[y][x] = self.__twoD[newY][newX]
        self.__twoD = new2D

    def counterClockwiseRotate(self,):
        '''
        The new 2d size is [max(oldY),max(oldX)]
        The nex 2d rules is
        newX=maxY-oldY
        newY=oldX
        '''
        new2D = self.__createRotate2D()
        for x in range(self.maxX()):
            for y in range(self.maxY()):
                newX = self.maxY()-y-1
                newY = x
                new2D[y][x] = self.__twoD[newY][newX]
        self.__twoD = new2D

    def maxX(self):
        return len(self.__twoD)

    def maxY(self):
        return len(self.__twoD[0])

    def point(self, x, y):
        return self.__twoD[x][y]

    def draw(self, twoD: List[List[int]] = None):
        if twoD == None:
            twoD = self.__twoD
        for yList in twoD:
            print(yList)
