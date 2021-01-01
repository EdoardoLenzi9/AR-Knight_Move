% domains

pos(1..n).
time(1..n**2).


% constraints
candidateStep(T,X + 2,Y + 1) :- occ(T,X,Y), time(T), pos(X + 2), pos(Y + 1).  
candidateStep(T,X + 2,Y - 1) :- occ(T,X,Y), time(T), pos(X + 2), pos(Y - 1).  
candidateStep(T,X + 1,Y + 2) :- occ(T,X,Y), time(T), pos(X + 1), pos(Y + 2).  
candidateStep(T,X + 1,Y - 2) :- occ(T,X,Y), time(T), pos(X + 1), pos(Y - 2).  
candidateStep(T,X - 1,Y + 2) :- occ(T,X,Y), time(T), pos(X - 1), pos(Y + 2).  
candidateStep(T,X - 1,Y - 2) :- occ(T,X,Y), time(T), pos(X - 1), pos(Y - 2).  
candidateStep(T,X - 2,Y + 1) :- occ(T,X,Y), time(T), pos(X - 2), pos(Y + 1).  
candidateStep(T,X - 2,Y - 1) :- occ(T,X,Y), time(T), pos(X - 2), pos(Y - 1).  


% Can't return to any place
occ(T+1,X,Y) :- step(T,X,Y), time(T), pos(X), pos(Y), time(T+1).
 :- occ(T1,X,Y), occ(T2,X,Y), T1 < T2, time(T1), time(T2).
 :- occ(T,X,Y), occ(T+1,X,Y), time(T), time(T+1), pos(X), pos(Y).


% At every time step choose a move
 :- step(T,X,Y), not candidateStep(T,X,Y), pos(X), pos(Y), time(T).
1 { step(T,X,Y) : pos(X), pos(Y) } 1 :- time(T).


%#show step/3.
#show occ/3.
%#show candidateStep/3.