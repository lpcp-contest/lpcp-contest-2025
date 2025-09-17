# City Lifelines

A violent storm has crippled the city.
Emergency Command must dispatch relief convoys from several depots to several hospitals scattered across the area.

The city's street map is provided as a graph:
vertices represent intersections, and edges represent streets.

Each convoy must travel along a **clear, simple path** from its assigned depot to its hospital.
However, the streets are so damaged and narrow that **no two convoys can use the same street** (if they do, both will be trapped in the debris).

Not every depot–hospital request can necessarily be served.
You may choose which pairs to serve.
Your task is to select the maximum number of pairs and assign to each a route such that:

* every route is a simple path between its depot and hospital, and
* no street is used by more than one route.

**Goal:** Serve as many depot–hospital pairs as possible using **edge-disjoint routes**.


## Special evaluation rules

You will get 0 points if your solution provides a wrong answer in any tested instance (as usual). 
Otherwise, you will get 1 point for each solved instance, unless another participant can provide a better solution than yours.

Stated differently, we don't strictly require to provide an optimal solution.
We will assign the point to the best solution we receive.


## Input Format

The first line contains three integers, `N M K`:

* `N` is the number of intersections in the city (vertices of the graph), labeled from `1` to `N`.
* `M` is the number of streets (edges of the graph).
* `K` is the number of depot–hospital requests.

The next `M` lines each contain two integers `U V`:

* indicating there is a two-way street between intersections `U` and `V`.

The next `K` lines each contain two integers `A B`:

* indicating a request to send a convoy from the depot at intersection `A` to the hospital at intersection `B`.


## Constraints

Instances are guaranteed to satisfy the following constraints:
- `N` does not exceed 196
- `M` does not exceed 220
- `K` does not exceed 34


## Output Format

The first line must be an integer, `P`, representing the number of depot–hospital pairs you have chosen to serve.

The next `P` lines must describe the route for each chosen pair.
Each route must be given as a sequence of intersection labels in visiting order, starting from the depot and ending at the hospital.

* Intersections are identified by their integer labels from `1` to `N` (as given in the input).
* Each route must correspond to a **simple path** in the city map (no repeated intersections).
* No street (edge) may appear in more than one route.


## Example

Instance in input:
```
6 7 3
1 2
2 3
3 4
4 5
5 6
2 5
1 6
1 4
2 6
3 5
```

Solution in output:
```
2
1 2 3 4
2 5 6
```




