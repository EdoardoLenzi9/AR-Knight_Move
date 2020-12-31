% params
int: k;   
int: n;                                             
int: max_time = n*n;   

% domains
set of int: CELL_DOMAIN     = 1..n;
set of int: TIME_DOMAIN     = 1..max_time;
set of int: BOOL            = 0..1;

% variables
var 1..max_time: halting_time1;     % knight 1 - halting time
var 1..max_time: halting_time2;     % knight 2 - halting time
var 1..max_time: visited_cells;     % maximization criterion: # visited cells

array[ CELL_DOMAIN, CELL_DOMAIN ] of     0..max_time: initial_occ;
array[ CELL_DOMAIN, CELL_DOMAIN ] of var 0..max_time: occ;           


% init positions and checkerboard O(n x n)
constraint forall(i, j in 1..n)(
    if initial_occ[i, j] > 0 then 
        occ[i, j] = initial_occ[i, j] 
    else 
        % a cell can be labeled with "1" only if initialized as 1
        occ[i, j] != 1 
    endif  
);


% turn constraint, one move per turn 
include "globals.mzn";
include "fzn_alldifferent_except.mzn";

predicate alldifferent_except_01(array[$X] of var int: vs) = 
   fzn_alldifferent_except(array1d(vs),{0, 1});

constraint alldifferent_except_01([ occ[i, j] | i,j in 1..n ]);
constraint forall(i,j in 1..n)(occ[i,j] <= visited_cells);


% motion pattern for knight 1
constraint forall(i, j in 1..n, t in 1..((n*n) div 2)-2) (
    (2*t) <= halting_time1  /\ 
    (2*t) <= halting_time2  /\
    occ[i,j] = (2*t)        ->  if i<n-1 /\ j<n   then (occ[i+2, j+1] = (2*t)+2) else false endif \/
                                if i<n-1 /\ j>1   then (occ[i+2, j-1] = (2*t)+2) else false endif \/
                                if i>2   /\ j<n   then (occ[i-2, j+1] = (2*t)+2) else false endif \/
                                if i>2   /\ j>1   then (occ[i-2, j-1] = (2*t)+2) else false endif \/
                                if i<n   /\ j<n-1 then (occ[i+1, j+2] = (2*t)+2) else false endif \/
                                if i<n   /\ j>2   then (occ[i+1, j-2] = (2*t)+2) else false endif \/
                                if i>1   /\ j<n-1 then (occ[i-1, j+2] = (2*t)+2) else false endif \/
                                if i>1   /\ j>2   then (occ[i-1, j-2] = (2*t)+2) else false endif \/
                                halting_time1 = (2*t) );


% motion pattern for knight 2
constraint forall(i, j in 1..n, t in 1..((n*n) div 2)-2) (
    ((2*t)+1) <= halting_time1  /\
    ((2*t)+1) <= halting_time2  /\
    occ[i,j] = ((2*t)+1)        ->  if i<n-1 /\ j<n   then (occ[i+2, j+1] = ((2*t)+3)) else false endif \/
                                    if i<n-1 /\ j>1   then (occ[i+2, j-1] = ((2*t)+3)) else false endif \/
                                    if i>2   /\ j<n   then (occ[i-2, j+1] = ((2*t)+3)) else false endif \/
                                    if i>2   /\ j>1   then (occ[i-2, j-1] = ((2*t)+3)) else false endif \/
                                    if i<n   /\ j<n-1 then (occ[i+1, j+2] = ((2*t)+3)) else false endif \/
                                    if i<n   /\ j>2   then (occ[i+1, j-2] = ((2*t)+3)) else false endif \/
                                    if i>1   /\ j<n-1 then (occ[i-1, j+2] = ((2*t)+3)) else false endif \/
                                    if i>1   /\ j>2   then (occ[i-1, j-2] = ((2*t)+3)) else false endif \/
                                    halting_time2 = ((2*t)+2)
);


% maximization criterion
visited_cells = min(halting_time1, halting_time2);


% search strategy
solve maximize visited_cells;

output  ["[["] ++ 
        [ if c = 1 /\ r != 1 then "\n" else if c = 1 /\ r = 1 then "" else "," endif endif ++
            show(occ[r,c]) | r in 1..n, c in 1..n] ++ 
        ["]]"];