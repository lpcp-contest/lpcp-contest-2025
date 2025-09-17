# 🧩 Reverse Puzzle: Bureaucratic Latin Square

The **Department of Grid Integrity** has already finalized the correct layout of the annual.
Our job, as the **Chief Minimalist Clue Auditor**, is to redact as much as possible, while still allowing the remaining clues to guarantee a unique reconstruction of the original (just enough to satisfy the auditors, and no more).

* Every number left in the grid is a **clue left unredacted**.
* The fewer clues you leave, the **fewer forms you have to file**.
* But beware: if there's more than one possible Latin square that fits your clues, your form gets bounced back.

> 🎯  __Objective__
>
> Given a **fully solved Latin square**, identify the **smallest possible set of clues** (pre-filled numbers) such that:
> * The given solution remains the **only** valid Latin square completion.
> * The number of pre-filled clues is **minimal** (cardinality-wise).

> 💡 __Latin Square Reminder__
>
> A Latin square of order `N` is an `N × N` grid filled with `N` symbols (usually numbers `1` to `N`) such that:
> * Each number appears exactly once in each **row**
> * Each number appears exactly once in each **column**


## Special evaluation rules

You will get 0 points if your solution provides a wrong answer in any tested instance (as usual). 
Otherwise, you will get 1 point for each solved instance, unless another participant can provide a better solution than yours.

Stated differently, we don't strictly require to provide an optimal solution.
We will assign the point to the best solution we receive.


## Input Format

The first line contains one integer, `N`, the size of the Latin Square.

The next `N` lines contain `N` integers each, representing the Latin Filing Matrix.
You could format this as:


## Output Format

`N` lines, each line containing `N` integers in the range `0..N`, with `0` denoting a redacted clue.


## Constraints

Instances are guaranteed to satisfy the following constraints:

* `N` does not exceed 9



## Example

Instance in input:
```
4
1 2 3 4
2 1 4 3
4 3 1 2
3 4 2 1
```

Solution in output:
```
1 0 0 0
0 0 4 0
0 0 0 0
3 0 0 1
```

