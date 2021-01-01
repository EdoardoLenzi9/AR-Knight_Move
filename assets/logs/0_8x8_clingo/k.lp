% domains

pos(1..n).
time(1..n**2).
knight(1..2).


% constraints
candidateStep(T,X + 2,Y + 1) :- occ(T,X,Y), time(T), pos(X + 2), pos(Y + 1), T > 1.  
candidateStep(T,X + 2,Y - 1) :- occ(T,X,Y), time(T), pos(X + 2), pos(Y - 1), T > 1.  
candidateStep(T,X + 1,Y + 2) :- occ(T,X,Y), time(T), pos(X + 1), pos(Y + 2), T > 1.  
candidateStep(T,X + 1,Y - 2) :- occ(T,X,Y), time(T), pos(X + 1), pos(Y - 2), T > 1.  
candidateStep(T,X - 1,Y + 2) :- occ(T,X,Y), time(T), pos(X - 1), pos(Y + 2), T > 1.  
candidateStep(T,X - 1,Y - 2) :- occ(T,X,Y), time(T), pos(X - 1), pos(Y - 2), T > 1.  
candidateStep(T,X - 2,Y + 1) :- occ(T,X,Y), time(T), pos(X - 2), pos(Y + 1), T > 1.  
candidateStep(T,X - 2,Y - 1) :- occ(T,X,Y), time(T), pos(X - 2), pos(Y - 1), T > 1.  

% halt propagation
halt(T + 1) :- halt(T), time(T), time(T + 1).
:- not_halt(T), halt(T).

% Se ho scelto un passo lo faccio
occ(T+2,X,Y) :- step(T,X,Y), time(T), pos(X), pos(Y), time(T+2).

% Non puo' essere che vado due volte sulla stessa posizione
 :- occ(T1,X,Y), occ(T2,X,Y), T1 < T2, time(T1), time(T2).

% non puo' essere che resto nella stessa posizione in T e T+2	
 :- occ(T,X,Y), occ(T+2,X,Y), time(T), time(T+2), pos(X), pos(Y).


% Non puo' essere che step non sia supportato da un candidate step
 :- step(T,X,Y), not candidateStep(T,X,Y), pos(X), pos(Y), time(T).
% Devo avere uno e un solo un step per turno
1 { step(T,X,Y) : pos(X), pos(Y) } 1 :- time(T).


%#show step/3.
#show occ/3.
%#show candidateStep/3.