from colorama import init as colorInit
from comp.Puzzle import Puzzle
from comp.Map import Map
from comp.Solutioner import Solutioner


def main():
    # just_fix_windows_console()
    colorInit()

    p1 = Puzzle([[0, 1], [1, 1]])
    p2 = Puzzle([[1, 1]])
    p3 = Puzzle([[1]])
    p4 = Puzzle([[0, 1], [1, 1], [0, 1]])
    m1 = Map([[-1, 0, 0, 0], [0, 0, 0, 0], [0, 0, -1, 0]])
    s1 = Solutioner(m1, [p1, p2, p3, p4])
    haveAnswer = s1.solve()
    print(haveAnswer)
    if haveAnswer:
        s1.printAnswer()
    # m1.draw()

    # answer =Map([[-1,2,3,1],[2,2,1,1],[4,4,-1,1]])
    # answer.draw()


if __name__ == "__main__":
    main()
