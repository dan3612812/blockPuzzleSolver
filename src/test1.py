from comp.Puzzle import Puzzle

twoD = [
    [0, 0, 0],
    [1, 1, 1],
    [0, 1, 1]
]


s = ""
n = 0b1
for y in twoD:
    for i in y:
        n = n << 1
        n = n | i

print("{0:b}".format(n))


exit()
p1 = Puzzle([[1, 0, 0], [1, 1, 1]])

p1.covertToBinary()
