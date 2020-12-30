# Counting Constraints

Count and restrict how many times certain values occur in an array of variables
If your model contains multiple counting constraints over the same array, constraints like distribute or global_cardinality below may be useful

predicate among(var int: n,                             # n variabili
                array [int] of var int: x,              # in x 
                set of int: v)                          # assumono un valore di v

function var int: among(array [int] of var int: x,      # ritorna quante variabili in x
                        set of int: v)                  # assumono un valore in v

predicate at_least(int: n,                              # al meno n variabili
                   array [int] of var set of int: x,    # in x
                   set of int: v)                       # assumono il valore v
predicate at_most( ... )

predicate at_most1(array [int] of var set of int: s)    # ogni coppia di set in s overlappa per al massimo un elemento

function var int: count(array [int] of var int: x,      # ritorna il numero di occorrenze di y in x
                        var int: y)

predicate count(array [int] of var int: x,              # vincola c ad essere 
                var int: y,                             # il numero di occorrenze di y
                var int: c)                             # in x
predicate count_eq(...)
predicate count_geq(...)                                # c >= del numero di y in x
predicate count_gt(...)
predicate count_leq(...)
predicate count_lt(...)
predicate count_neq(...)

predicate distribute(array [int] of var int: card,      # card[i] dev'essere = numero di occorrenze di 
                     array [int] of var int: value,     # value[i] in 
                     array [int] of var int: base)      # base

function array [int] of var int: distribute(array [int] of var int: value,  # ritorna card invece che
                                            array [int] of var int: base)   # usarla come constraint

predicate exactly(int: n,                               # n variabili in 
                  array [int] of var set of int: x,     # x devono avere valore
                  set of int: v)                        # v

predicate global_cardinality(array [int] of var int: x,                         # counts[i] = # di occorrenze di cover[i] in x
                             array [int] of int: cover,
                             array [int] of var int: counts)
function array [int] of var int: global_cardinality(array [int] of var int: x,  # ritorna counts
                                                    array [int] of int: cover)
predicate global_cardinality_closed(array [int] of var int: x,              # stessa cosa
function ... global_cardinality_closed(array [int] of var int: x,           # 


predicate global_cardinality_low_up(array [int] of var int: x,              # cover[i] compare [lbound[i], ubound[i]] volte in x
                                    array [int] of int: cover,
                                    array [int] of int: lbound,
                                    array [int] of int: ubound)
predicate global_cardinality_low_up_closed                                  # stessa roba


# All-Different and related constraints

predicate all_different(array [$X] of var int: x)
predicate all_different(array [$X] of var set of int: x)
predicate all_disjoint(array [$X] of var set of int: S)             # gli insiemi in S (insieme di insiemi) sono disgiunti a coppie
predicate all_equal(array [$X] of var int: x)                       # tutti valori uguali   
predicate all_equal(array [$X] of var set of int: x)            
predicate alldifferent_except_0(array [$X] of var int: vs)          # tutti diversi tranne gli zeri
predicate nvalue(var int: n, array [int] of var int: x)             # ci devono essere esattamente n valori diversi in x
function var int: nvalue(array [int] of var int: x)                 # ritorna il numero di valori distinti in x
predicate symmetric_all_different(array [int] of var int: x)        # x all_different e per ogni i, x[i]=j -> x[j]=i


# Lexicographic constraints

predicate lex2(array [int,int] of var int: x)               # righe e colonne adiacenti in x devono essere ordinate lessicograficamente
                                                            # possono avere lo stesso valore
predicate strict_lex2(array [int,int] of var int: x)        # come lex2 ma non posso avere lo stesso valore

predicate lex_greater(array [int] of var bool: x,           # array x STRETTAMENTE maggiore di y lessicograficamente
                      array [int] of var bool: y)           # compara i due elementwise in modo non ordinato
predicate lex_greater( int, float, set)

predicate lex_greatereq
predicate lex_less
predicate lex_lesseq

predicate seq_precede_chain(array [int] of var int: x)                      # richiede che i preceda i+1 in x per ogni i positivo
predicate seq_precede_chain(array [int] of var set of int: x)               # in un set di array invece che in uno solo


predicate value_precede(int: s, int: t, array [int] of var int: x)          # richiede che s preceda t in x 
predicate value_precede(int: s, int: t, array [int] of var opt int: x)      # quindi se ho un t in x -> deve esserci un s prima

predicate value_precede_chain(array [int] of int: c,                        # richiede che c[i] preceda c[i+1] in x
                              array [int] of var int: x)
predicate value_precede_chain(array [int] of int: c,                        # uguale ma con i set
                              array [int] of var set of int: x) 


# Sorting constraints

function array [int] of var int: arg_sort(array [int] of var int: x)        # ritorna una permutazione di p / x e' sortato in ordine p
                                                                            # forall i, x[p[i]] <= x[p[i+1]]
function array [int] of var int: arg_sort(array [int] of var float: x)      # uguale con i float

predicate arg_sort(array [int] of var int: x,                               # vincolo / p dev'essere argsort valido di x
                   array [int] of var int: p)
predicate arg_sort(array [int] of var float: x,                             # uguale con float
                   array [int] of var int: p)

predicate decreasing(array [int] of var bool: x)                            # x in decreasing order (dup allowed)
predicate decreasing(array [int] of var float: x)
predicate decreasing(array [int] of var int: x)
predicate decreasing(array [int] of var set of int: x)

predicate increasing(array [int] of var bool: x)                            # x in increasing order (dup allowed)
predicate increasing(array [int] of var float: x)
predicate increasing(array [int] of var int: x)
predicate increasing(array [int] of var set of int: x)

predicate sort(array [int] of var int: x, array [int] of var int: y)        # y (multiset) e' la versione di x sortata
function array [int] of var int: sort(array [int] of var int: x)            # ritorna y

predicate strictly_increasing(array [int] of var bool: x)                   # vincola x come sortato in ordine strettamente crescente 
predicate strictly_increasing(array [int] of var int: x)                    # (no dups)
predicate strictly_increasing(array [int] of var opt int: x)


# Channeling constraints

predicate int_set_channel(array [int] of var int: x,                    # ( x[i] = j ) ↔ ( i in y[j]).
                          array [int] of var set of int: y) 

predicate inverse(array [int] of var int: f,                            # vincola due array
                  array [int] of var int: invf)                         # ad essere l'una la fn inversa dell'altra

function array [$$E] of var $$F: inverse(array [$$F] of var $$E: f)     # ritorna la funzione inversa
function array [$$E] of $$F: inverse(array [$$F] of $$E: f)         

predicate inverse_in_range(array [int] of var int: f,                   # boh
                           array [int] of var int: invf)
predicate inverse_set(array [int] of var set of int: f,
                      array [int] of var set of int: invf)

predicate link_set_to_booleans(var set of int: s,                       # array di bool b deve rappresentare il set s /
                               array [int] of var bool: b)              # i in s ↔ b [ i ]

# Packing constraints

predicate bin_packing(int: c,                                           # ogni item con peso w[i] deve essere ficcato nel 
                      array [int] of var int: bin,                      # bin[i]
                      array [int] of int: w)                            # senza eccedere la capacita' c per bin

predicate bin_packing_capa(array [int] of int: c,                       # capacita' diverse per bin (upper bound)
                           array [int] of var int: bin,
                           array [int] of int: w)

predicate bin_packing_load(array [int] of var int: load,                # la somma dei pesi deve essere uguale a load
                           array [int] of var int: bin,                 # non e' un upperbound
                           array [int] of int: w)

function array [int] of var int: bin_packing_load(array [int] of var int: bin,  # ritorna load
                                                  array [int] of int: w)

predicate diffn(array [int] of var int: x,      # non overlappings rectangles with coords (x,y)(dx,dy)
                array [int] of var int: y,      # 0-width rectangles can still not overlap with any other rectangle
                array [int] of var int: dx,
                array [int] of var int: dy)
predicate diffn_nonstrict(array [int] of var int: x,                # 0-width rectangles can overlap
                          array [int] of var int: y,
                          array [int] of var int: dx,
                          array [int] of var int: dy)
                          
predicate diffn_k(array [int,int] of var int: box_posn,             # constrains k-dimensional boxes to be non overlapping
                  array [int,int] of var int: box_size)
predicate diffn_nonstrict_k(array [int,int] of var int: box_posn,   # 0-width boxes can overlap
                            array [int,int] of var int: box_size)

predicate geost(int: k,                                             # un non-overlapping constraint per oggetti k dimensionali
                array [int,int] of int: rect_size,
                array [int,int] of int: rect_offset,
                array [int] of set of int: shape,
                array [int,int] of var int: x,
                array [int] of var int: kind)

predicate geost_bb(int: k,                                          # come prima ma il tutto deve fittare una k-dimensional bounding box
                   array [int,int] of int: rect_size,
                   array [int,int] of int: rect_offset,
                   array [int] of set of int: shape,
                   array [int,int] of var int: x,
                   array [int] of var int: kind,
                   array [int] of var int: l,
                   array [int] of var int: u)

predicate geost_nonoverlap_k(array [int] of var int: x1,            # 2D objects don't overlap
                             array [int] of int: w1,                # and 0-length obj don't appear in the middle of other objects
                             array [int] of var int: x2,
                             array [int] of int: w2)

predicate geost_smallest_bb(int: k,                                 # come prima ma ora la bounding box e' la minima possibile
                            array [int,int] of int: rect_size,      # (ogni lato tocca un oggetto)
                            array [int,int] of int: rect_offset,
                            array [int] of set of int: shape,
                            array [int,int] of var int: x,
                            array [int] of var int: kind,
                            array [int] of var int: l,
                            array [int] of var int: u)

predicate knapsack(array [int] of int: w,           # knapsak with wheight w
                   array [int] of int: p,           # profit p
                   array [int] of var int: x,       # number of picked items
                   var int: W,                      # sum sizes
                   var int: P)                      # total profit


# Scheduling constraints

predicate alternative(var opt int: s0,                      # ???
                      var int: d0,
                      array [int] of var opt int: s,
                      array [int] of var int: d)
predicate span(var opt int: s0,
               var int: d0,
               array [int] of var opt int: s,
               array [int] of var int: d)

predicate cumulative(array [int] of var int: s,             # a set of tasks with start times s, 
                     array [int] of var int: d,             # duration d
                     array [int] of var int: r,             # resource requirements r
                     var int: b)                            # never require more than a global bound b at any time
predicate cumulative(array [int] of var opt int: s,         # start time optional => ignore absent tasks
                     array [int] of var int: d,             # durations
                     array [int] of var int: r,             # requirements
                     var int: b)

predicate disjunctive(array [int] of var int: s,            # non overlapping in time tasks
                      array [int] of var int: d)
predicate disjunctive(array [int] of var opt int: s,        # optional
                      array [int] of var int: d)

predicate disjunctive_strict(array [int] of var int: s,     # no tasks with 0 duration
                             array [int] of var int: d)
predicate disjunctive_strict(array [int] of var opt int: s, # optional
                             array [int] of var int: d)


# Graph constraints
                                                            # dato un grafo trova un cammino da s a t di peso k
predicate bounded_dpath(int: N,                             # numero di nodi
                        int: E,                             # numero di archi
                        array [int] of int: from,           # nodo target per ogni edge
                        array [int] of int: to,             # nodo di partenza di ogni edge
                        array [int] of int: w,              # peso di ogni edge
                        var int: s,                         # source node
                        var int: t,                         # destination node
                        array [int] of var bool: ns,        # bool che mi dice se il nodo e' nel subgraph
                        array [int] of var bool: es,        # bool che mi dice se l'arco e' nel subgraph
                        var int: K)                         # il costo del path
predicate bounded_dpath(array [int] of $$N: from,
                        array [int] of $$N: to,
                        array [int] of int: w,
                        var $$N: s,
                        var $$N: t,
                        array [$$N] of var bool: ns,
                        array [int] of var bool: es,
                        var int: K)

predicate bounded_path(int: N,                              # undirected
                       int: E,
                       array [int] of int: from,
                       array [int] of int: to,
                       array [int] of int: w,
                       var int: s,
                       var int: t,
                       array [int] of var bool: ns,
                       array [int] of var bool: es,
                       var int: K)
predicate bounded_path(array [int] of $$N: from,
                       array [int] of $$N: to,
                       array [int] of int: w,
                       var $$N: s,
                       var $$N: t,
                       array [$$N] of var bool: ns,
                       array [int] of var bool: es,
                       var int: K)

predicate connected(array [int] of $$N: from,               # trova il sottografo connesso
                    array [int] of $$N: to,
                    array [$$N] of var bool: ns,
                    array [int] of var bool: es)

predicate d_weighted_spanning_tree(int: N,                              # es set of edges dev'essere weighted spanning tree
                                   int: E,                              # con root in r e peso w
                                   array [int] of int: from,
                                   array [int] of int: to,
                                   array [int] of int: w,
                                   var int: r,
                                   array [int] of var bool: es,
                                   var int: K)

predicate dag(array [int] of $$N: from,                                 # constrains to be a DAG (acyclic graph)
              array [int] of $$N: to,
              array [$$N] of var bool: ns,
              array [int] of var bool: es)

predicate dconnected(array [int] of $$N: from,                          # constrains a d(irected) graph to be connected
                     array [int] of $$N: to,
                     array [$$N] of var bool: ns,
                     array [int] of var bool: es)

predicate dpath(int: N,
                int: E,
                array [int] of int: from,
                array [int] of int: to,
                var int: s,
                var int: t,
                array [int] of var bool: ns,                            # constrains the subgraph ns and es of a given directed graph
                array [int] of var bool: es)                            # to be a path from s to t
predicate dpath(array [int] of $$N: from,
                array [int] of $$N: to,
                var $$N: s,
                var $$N: t,
                array [$$N] of var bool: ns,
                array [int] of var bool: es)

predicate dreachable(int: N,                                            # constrains a directed graph to be reachable from r
                     int: E,
                     array [int] of int: from,
                     array [int] of int: to,
                     var int: r,
                     array [int] of var bool: ns,
                     array [int] of var bool: es)
predicate dreachable(array [int] of $$N: from,
                     array [int] of $$N: to,
                     var $$N: r,
                     array [$$N] of var bool: ns,
                     array [int] of var bool: es)

predicate dsteiner(int: N,                                              # weighted spanning tree rooted in r and weighted by w
                   int: E,
                   array [int] of int: from,
                   array [int] of int: to,
                   array [int] of int: w,
                   var int: r,
                   array [int] of var bool: ns,
                   array [int] of var bool: es,
                   var int: K)

predicate dtree(int: N,                                                 # find a tree rooted in r
                int: E, 
                array [int] of int: from,
                array [int] of int: to,
                var int: r,
                array [int] of var bool: ns,
                array [int] of var bool: es)
predicate dtree(array [int] of $$N: from,
                array [int] of $$N: to,
                var $$N: r,
                array [$$N] of var bool: ns,
                array [int] of var bool: es)

predicate path                                                          # la stessa cosa su grafi indiretti
predicate reachable
predicate steiner
predicate subgraph
predicate tree
predicate weighted_spanning_tree

# Extensional constraints (table, regular etc.)

predicate cost_mdd(array [int] of var int: x,               # x dev'essere una path di costo MDD con total weight totalcost
                   int: N,
                   array [int] of int: level,
                   int: E,
                   array [int] of int: from,
                   array [int] of set of int: label,
                   array [int] of int: cost,
                   array [int] of int: to,
                   var int: totalcost)

predicate cost_regular(array [int] of var int: x,           # tipo una macchiana a stati
                       int: Q,
                       int: S,
                       array [int,int] of int: d,
                       int: q0,
                       set of int: F,
                       array [int,int] of int: c,
                       var int: C)

predicate mdd(array [int] of var int: x,
              int: N,
              array [int] of int: level,
              int: E,
              array [int] of int: from,
              array [int] of set of int: label,
              array [int] of int: to)

predicate mdd_nondet(array [int] of var int: x,
                     int: N,
                     array [int] of int: level,
                     int: E,
                     array [int] of int: from,
                     array [int] of set of int: label,
                     array [int] of int: to)

predicate regular(array [int] of var int: x,
                  int: Q,
                  int: S,
                  array [int,int] of int: d,
                  int: q0,
                  set of int: F)

predicate regular(array [int] of var int: x,
                  int: Q,
                  set of int: S,
                  array [int,int] of int: d,
                  int: q0,
                  set of int: F)

predicate regular(array [int] of var int: x, string: r)

predicate regular_nfa(array [int] of var int: x,
                      int: Q,
                      int: S,
                      array [int,int] of set of int: d,
                      int: q0,
                      set of int: F)

predicate regular_nfa(array [int] of var int: x,
                      int: Q,
                      set of int: S,
                      array [int,int] of set of int: d,
                      int: q0,
                      set of int: F)

predicate table(array [int] of var bool: x, array [int,int] of bool: t)

predicate table(array [int] of var int: x, array [int,int] of int: t)

predicate table(array [int] of var opt int: x,
                array [int,int] of opt int: t)


# Machine learning constraints

predicate neural_net(array [int] of var float: inputs,
                     array [int] of int: input_ids,
                     array [int] of var float: outputs,
                     array [int] of int: output_ids,
                     array [int] of float: bias,
                     array [int] of float: edge_weight,
                     array [int] of int: edge_parent,
                     array [int] of int: first_edge,
                     NEURON_TYPE: neuron_type)



# Potenzialmente utili

among(n, x, v)		n variabili in x assumono un valore di v
count(x, y, c)		c = numero occorenze y in x 
distribute(x, y, x)	come prima ma c e' un array e y un array
exactly

all_different
nvalue			ci devono essere esattamente n valori diversi in x

lexicographic constraints 
packing constraints