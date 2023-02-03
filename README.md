# block puzzle solver
<!-- ![image](https://user-images.githubusercontent.com/30949254/216652270-a97a00b9-d0e9-4c94-a238-294fc9a4a00d.png){: width="50%"} -->
<img src="https://user-images.githubusercontent.com/30949254/216652270-a97a00b9-d0e9-4c94-a238-294fc9a4a00d.png" width="250" height="250">

# Description
To solve block puzzle game.

Support rotate a puzzle.

Support have obstacle in map.

# Usage

Run this command `python src/index.py`.

You can custom them! follow along.

Set the Map and Puzzles in  `main` of `src/index.py`.
if the puzzle like this
```
 ⬛⬛⬛
 ⬛
```
block =1 empty=0 in 2d array,the puzzle code is
```
Puzzle([
[1,1,1]
[1,0,0]
])
```

Is same with Map. empty=0, obstacle=1.

Then talk the Map and Puzzles to Solutioner.
```
Solutioner(map,[puzzleA,puzzleB,...])
```
Call `solutioner.solve()` return True when it have answer.

Then call the `solutioner.printAnswer()`to print answer graph.

# TODO
1. Use bitmask to optimize performance.
2. Use multiprocessing.
