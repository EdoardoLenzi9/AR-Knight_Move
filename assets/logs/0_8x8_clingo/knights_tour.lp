% domains

pos(1..n).
time(1..n**2).


% constraints

candidateStep(T,X + 2,Y + 1) :- position(T,X,Y), time(T), pos(X + 2), pos(Y + 1).  
candidateStep(T,X + 2,Y - 1) :- position(T,X,Y), time(T), pos(X + 2), pos(Y - 1).  
candidateStep(T,X + 1,Y + 2) :- position(T,X,Y), time(T), pos(X + 1), pos(Y + 2).  
candidateStep(T,X + 1,Y - 2) :- position(T,X,Y), time(T), pos(X + 1), pos(Y - 2).  
candidateStep(T,X - 1,Y + 2) :- position(T,X,Y), time(T), pos(X - 1), pos(Y + 2).  
candidateStep(T,X - 1,Y - 2) :- position(T,X,Y), time(T), pos(X - 1), pos(Y - 2).  
candidateStep(T,X - 2,Y + 1) :- position(T,X,Y), time(T), pos(X - 2), pos(Y + 1).  
candidateStep(T,X - 2,Y - 1) :- position(T,X,Y), time(T), pos(X - 2), pos(Y - 1).  


% Can't return to any place
position(T+1,X,Y) :- step(T,X,Y), time(T), pos(X), pos(Y), time(T+1).
 :- position(T1,X,Y), position(T2,X,Y), T1 < T2, time(T1), time(T2).
 :- position(T,X,Y), position(T+1,X,Y).


% At every time step choose a move
 :- step(T,X,Y), not candidateStep(T,X,Y), pos(X), pos(Y), time(T).
1 { step(T,X,Y) : pos(X), pos(Y) } 1 :- time(T).


%#show step/3.
#show position/3.
%#show candidateStep/3.