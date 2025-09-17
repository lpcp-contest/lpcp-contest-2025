# Leaper Tours on Toroidal Boards

**Leapers** are non-standard chess figures, of which the knight is a special case. They move n fields in one direction (horizontal or vertical) and m fields in the other direction. As the name suggest, they "leap" over any intermediate fields, so it is sufficient to consider only the starting and landing field for one move. We will denote the kind of piece (p,q)-leaper, where p and q denote the offset to the landing field. We will only consider symmetric leapers, which means that the initial direction can be vertical or horizontal (as for the standard knight piece), so we assume p<=q. A standard knight is therefore a (1,2)-leaper.

We will also consider non-standard toroidal boards of variable size.
A **Toroidal Board** of size (n,m), so with n "rows" and m "columns", can be thought of as a rectangular chess board of size (n,m), but consider the board to be bent along its vertical axis such that the right hand side is glued to its left hand side, and additionally it is also bent along its horizontal axis with its top glued to the bottom. So, fields (j,m) are next to (j,1), and fields (n,k) are next to (1,k). Another way of picturing this is a doughnut-shaped board. Here is a link to a picture created with chatgpt: 
https://chatgpt.com/s/m_68c4313162d88191a757745ed009339a

The problem to solve is whether there exists an (i,j)-leaper tour on a given toroidal board of size (n,m). A tour is a sequence of leaper moves that visits each field exactly once and eventually returns to the starting position. This extends the classic knight tour: it is a (1,2)-leaper tour on an (8,8) non-toroidal standard board.

## Input Format

The first line contains two positive integers separated by a space, `N` and `M`, the dimension of the Toroidal Board.

The second line also contains two positive integers separated by a space, `P` and `Q`, describing the move of the leaper, with `P` <= `Q`.

## Output Format

Lines with four integers separated by a space, `A B C D`, indicating a leaper move from (`A`,`B`) to (`C`,`D`). The moves should form a tour, but do not have to be provided in any specific order.

## Example

Instance in input:
```
2 2
1 2
```

Solution in output:
```
1 1 1 2
1 2 2 2
2 1 1 1
2 2 2 1
```
