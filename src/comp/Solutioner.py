from typing import List, Any
from .Map import Map
from .Puzzle import Puzzle
from itertools import permutations


class Solutioner:
    def __init__(self, map: Map, puzzles: List[Puzzle], rotate: bool = False, verbose: bool = False) -> None:
        self.map = map
        self.puzzles = puzzles
        self.rotate = rotate
        self.rotateCount = 1
        self.verbose = verbose
        if self.rotate:
            self.rotateCount = 4

    def solve(self):
        puzzlesCount = len(self.puzzles)
        perms = permutations(list(range(0, puzzlesCount)))
        for ind, perm in enumerate(perms):
            if self.verbose:
                print("try ", ind, "  ", perm)
            for index, puzzleIndex in enumerate(perm):
                nowPuzzle = self.puzzles[puzzleIndex]
                needBreak = False
                for rotateSerial in range(0, self.rotateCount):
                    canPut = self.map.autoPutIn(nowPuzzle)
                    if canPut == False:
                        if self.rotate:
                            if rotateSerial == self.rotateCount-1:
                                needBreak = True
                                break
                            nowPuzzle.clockwiseRotate()
                            continue
                        else:
                            needBreak = True
                            break
                    else:
                        if self.verbose:
                            self.map.draw()
                            print("----------------")
                        if puzzlesCount-1 == index:
                            print("get answer")
                            return True
                        break
                if needBreak:
                    break
            self.map.clean()
            if self.verbose:
                print("clean map try next the permutation")
        return False

    def printAnswer(self,) -> None:
        self.map.draw()

    def rotateLeft(self, array: List[Any]) -> None:
        firstElement = array.pop(0)
        array.append(firstElement)
