# Discrete Tomography

You need to find out what is inside a box, but are not allowed to open it. You can, however, measure densities across the box, like a tomograph. We have done this for one slice - can you reconstruct the object inside? Assume that the object slice inside is connected (one piece, diagonal connections are OK) and convex (no holes). All densities (measured and in the object) are non-negative integers. The sums of the reconstructed object densities in each row and column must match the measurements.


## Input Format

The first line contains two positive integers separated by a space, `R`, the number of rows, and `C`, the number of columns of the rectangular slice.

The second line contains `R` non-negative integers (separated by spaces), which are the measured densities of the rows (in ascending order).

The third line contains `C` non-negative integers (separated by spaces), which are the measured densities of the columns (in ascending order).

## Output Format

`R` lines containing `C` non-negative integers each. All non-zero entries must be connected (horizontally, vertically, or diagonally) and there must not be any holes.

## Example

Instance in input:
```
2 3
1 2
1 2 0
```

Solution in output:
```
1 0 0
0 2 0
```

There is one other solution in this case:
```
0 1 0
1 1 0
