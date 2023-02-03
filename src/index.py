from time import time
from colorama import init as colorInit
from comp.Puzzle import Puzzle
from comp.Map import Map
from comp.Solutioner import Solutioner


def main():
    # just_fix_windows_console()
    colorInit()

    p1 = Puzzle([[0, 1], [1, 1], [1, 1]])
    p2 = Puzzle([[1, 1, 0], [0, 1, 1]])
    p3 = Puzzle([[1, 1], [0, 1]])
    p4 = Puzzle([[1, 1], [0, 1], [0, 1], [0, 1],])
    p5 = Puzzle([[1, 0], [1, 1], [1, 0]])
    p6 = Puzzle([[1, 0, 0], [1, 1, 0], [0, 1, 1]])
    p7 = Puzzle([[1], [1]])
    p8 = Puzzle([[0, 0, 1], [0, 0, 1], [1, 1, 1],])
    p9 = Puzzle([[1, 0, 0], [1, 1, 1]])
    m1 = Map([[-1, 0, 0, 0, 0, 0],
              [0, 0, -1, 0, 0, 0],
              [0, 0, 0, 0, 0, -1],
              [0, -1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, -1, 0],
              [0, 0, 0, 0, 0, 0],])
    s1 = Solutioner(m1, [p2, p1, p3, p4, p5, p6, p9, p7, p8], False, True)
    startTime = time()
    haveAnswer = s1.solve()
    endTime = time()
    print("running time %f seconds" % (endTime-startTime))
    if haveAnswer:
        print("==============")
        s1.printAnswer()
        print("==============")
    # m1.draw()

    # answer =Map([[-1,2,3,1],[2,2,1,1],[4,4,-1,1]])
    # answer.draw()


if __name__ == "__main__":
    main()
