# 🧠 Professors vs. Students: The Campus Conundrum

You are designing a winding fence around the secretive **Professors' Lounge**. 
The fence must keep **professors (🧛‍♀️)** safely enclosed **inside**, while **students (🧟‍♀️)** eager for office hours are left **outside**.

The finished fence must form **one continuous loop**, a closed circuit that does **not touch or cross itself**.

* A **black circle** represents a spot where the fence must make a **90° turn**, and it must be flanked by straight segments on both sides. This is a formal, rule-bound transition.

* A **white circle** represents a more relaxed rule: the fence must continue **straight through**, but must also make at least one **turn** immediately before or after the circle.

* Cells marked with **dotted circles** are **outposts** located **inside** the fence. 
  Each outpost must be able to **see** a number of cells equal to the digit shown (counting **up, down, left, and right**, including the outpost itself) before a fence segment blocks the view in each direction.
  _In other words, the number tells how many cells are visible **from the outpost** (not counting diagonals), until hitting a fence in each direction._

* Cells with **uncircled digits** represent **administrative staff** enforcing **vague procedural rules** that nobody fully understands (not even themselves).
  Each administrator insists on being surrounded by **exactly as many fence segments** as the number on their desk... for reasons buried deep in a filing cabinet no one's allowed to open.
  They might be **inside or outside** the fence (that part was left ambiguous in the memo). 
  _The only thing everyone agrees on: **get the number of fence segments right**, or face paperwork._


## Input Format

The first line contains eight integers, `Nr Nc P S B W O A`:
- `Nr Nc` determine the size of the campus (a rectangle of `Nr` rows and `Nc` columns)
- `P` is the number of professors
- `S` is the number of students
- `B` is the number of black circles
- `W` is the number of white circles
- `O` is the number of outposts
- `A` is the number of administrative staff

After that there are
- `P` lines `R C` representing a professor located at row `R` and column `C`
- `S` lines `R C` representing a student located at row `R` and column `C`
- `B` lines `R C` representing a black circle centered around locations (`R-1`,`C-1`), (`R-1`,`C`), (`R`,`C-1`) and (`R`,`C`)
- `W` lines `R C` representing a white circle centered around locations (`R-1`,`C-1`), (`R-1`,`C`), (`R`,`C-1`) and (`R`,`C`)
- `O` lines `R C V` representing an outpost located at row `R` and column `C`, with `V` being the number of visible cells
- `A` lines `R C V` representing an administrative staff located at row `R` and column `C`, with `V` being the number of surrounding fence segments.


## Output Format

The first line must be an integer, `F`, representing the number of fence segments.

The next `F` lines must have the form `R C R' C'`, representing a fence segmnet (of length 1) connecting the points centered around locations
- (`R-1`,`C-1`), (`R-1`,`C`), (`R`,`C-1`) and (`R`,`C`)
- (`R'-1`,`C'-1`), (`R'-1`,`C'`), (`R'`,`C'-1`) and (`R'`,`C'`)


## Constraints

Instances are guaranteed to satisfy the following constraints:
- `Nr` does not exceed 15
- `Nc` does not exceed 27


## Example

Instance in input:
```
8 8 2 1 3 7 1 9
6 3
8 7
2 2
4 8
7 1
7 9
2 5
2 7
3 1
4 9
5 3
5 9
7 7
8 2 4
3 5 0
3 1 1
5 1 1
8 1 1
1 4 2
4 1 2
1 5 3
1 7 3
4 6 3
```

Solution in output:
```
72
1 3 1 4
1 3 2 3
1 4 2 4
1 5 1 6
1 5 2 5
1 6 2 6
1 7 1 8
1 7 2 7
1 8 2 8
2 1 2 2
2 1 3 1
2 2 3 2
2 3 3 3
2 4 3 4
2 5 3 5
2 6 3 6
2 7 3 7
2 8 3 8
3 1 4 1
3 2 3 3
3 4 3 5
3 6 3 7
3 8 3 9
3 9 4 9
4 1 5 1
4 2 4 3
4 2 5 2
4 3 4 4
4 4 4 5
4 5 5 5
4 6 4 7
4 6 5 6
4 7 4 8
4 8 5 8
4 9 5 9
5 1 6 1
5 2 5 3
5 3 5 4
5 4 6 4
5 5 6 5
5 6 5 7
5 7 6 7
5 8 6 8
5 9 6 9
6 1 7 1
6 4 7 4
6 5 7 5
6 6 6 7
6 6 7 6
6 8 6 9
7 1 7 2
7 2 7 3
7 3 7 4
7 5 8 5
7 6 7 7
7 7 7 8
7 8 7 9
7 9 8 9
8 2 8 3
8 2 9 2
8 3 8 4
8 4 8 5
8 6 8 7
8 6 9 6
8 7 9 7
8 9 9 9
9 2 9 3
9 3 9 4
9 4 9 5
9 5 9 6
9 7 9 8
9 8 9 9
```
