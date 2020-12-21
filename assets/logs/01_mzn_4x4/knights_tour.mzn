% params
int: n;                                             
int: max_time = n*n;   

% domains
set of int: CELL_DOMAIN     = 1..n;
set of int: TIME_DOMAIN     = 1..max_time;
set of int: BOOL            = 0..1;

% variables
var 1..n*n: halting_time;
var 1..n*n: visited_cells;

array[ CELL_DOMAIN, CELL_DOMAIN ] of 0..n*n:      initial_occ;
array[ CELL_DOMAIN, CELL_DOMAIN ] of var 0..n*n:  occ;           


% init posizione e scacchiera 
constraint forall(i, j in 1..n)(
    if initial_occ[i, j] > 0 then occ[i, j] = initial_occ[i, j] else occ[i, j] != 1 endif  
);

/*
% mossa cavallo
constraint forall(i, j in 1..n, t in 2..(n*n)-1) (
    t <= halting_time /\ occ[i,j] = t -> if i<n-1 /\ j<n   then (occ[i+2, j+1] = t+1) else false endif \/
                                         %if i<n-1 /\ j>1   then (occ[i+2, j-1] = t+1) else false endif \/
                                         if i>2   /\ j<n   then (occ[i-2, j+1] = t+1) else false endif \/
                                         %if i>2   /\ j>1   then (occ[i-2, j-1] = t+1) else false endif \/
                                         if i<n   /\ j<n-1 then (occ[i+1, j+2] = t+1) else false endif \/
                                         if i<n   /\ j>2   then (occ[i+1, j-2] = t+1) else false endif \/
                                         if i>1   /\ j<n-1 then (occ[i-1, j+2] = t+1) else false endif \/
                                         if i>1   /\ j>2   then (occ[i-1, j-2] = t+1) else false endif \/
                                         halting_time = t+1
);
*/

constraint occ[n,n] = 15;

constraint forall(i, j in 1..n, t in 2..(n*n)-1) (
    t <= halting_time /\ occ[i,j] = t -> if i<n then (occ[ i+1, j   ] = t+1) else false endif \/
                                         if i>1 then (occ[ i-1, j   ] = t+1) else false endif \/
                                         if j<n then (occ[ i,   j+1 ] = t+1) else false endif \/
                                         if j>1 then (occ[ i,   j-1 ] = t+1) else false endif \/
                                         halting_time = t+1
);


constraint forall(i,j in 1..n)(
    occ[i,j] <= halting_time
);


visited_cells = sum(i,j in 1..n) (if occ[i,j] != 0 /\ occ[i,j] <= halting_time then 1 else 0 endif);
constraint visited_cells <= halting_time;

solve maximize visited_cells;
%solve satisfy;

%output [ 
%    show(visited_cells) ++ "\n" ++
%    show(halting_time) ++ "\n" ++
%    show([if c = 1 then "\n" else " " endif ++
%        show(occ[r,c])
%    | r in 1..n, c in 1..n]) ];

output [ if c = 1 then "\n" else " " endif ++
        show(occ[r,c])
    | r in 1..n, c in 1..n];