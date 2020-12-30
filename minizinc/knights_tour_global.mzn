include "globals.mzn";
include "fzn_alldifferent_except.mzn";

predicate alldifferent_except_01(array[$X] of var int: vs) = 
   fzn_alldifferent_except(array1d(vs),{0, 1});

% params
int: k;   
int: n;                                             
int: max_time = n*n;   

% domains
set of int: CELL_DOMAIN     = 1..n;
set of int: TIME_DOMAIN     = 1..max_time;
set of int: BOOL            = 0..1;

% variables
var 1..n*n: halting_time1;
var 1..n*n: halting_time2;
var 1..n*n: visited_cells;

array[ CELL_DOMAIN, CELL_DOMAIN ] of 0..n*n:      initial_occ;
array[ CELL_DOMAIN, CELL_DOMAIN ] of var 0..n*n:  occ;           


% init posizione e scacchiera 
constraint forall(i, j in 1..n)(
    if initial_occ[i, j] > 0 then 
        occ[i, j] = initial_occ[i, j] 
    else 
        occ[i, j] != 1 % non puo' essere 1 a meno di init
    endif  
);


constraint alldifferent_except_01([ occ[i, j] | i,j in 1..n ]);

visited_cells = sum(i,j in 1..n) (if occ[i,j] != 0 then 1 else 0 endif);

solve :: int_search(occ, [[varchoice]], [[constrainchoice]], [[strategy]])
    maximize visited_cells; 

%solve :: int_search(occ, smallest, indomain_min, complete)
%    maximize visited_cells; 
      
%solve maximize visited_cells;
%solve satisfy;

%output [ 
%    show(visited_cells) ++ "\n" ++
%    show(halting_time) ++ "\n" ++
%    show([if c = 1 then "\n" else " " endif ++
%        show(occ[r,c])
%    | r in 1..n, c in 1..n]) ];

output  ["[["] ++ 
        [ if c = 1 /\ r != 1 then "\n" else if c = 1 /\ r = 1 then "" else "," endif endif ++
            show(occ[r,c]) | r in 1..n, c in 1..n] ++ 
        ["]]"];