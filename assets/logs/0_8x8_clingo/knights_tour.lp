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

% Se ho scelto un passo lo faccio
occ(T+2,X,Y) :- step(T,X,Y), time(T), pos(X), pos(Y), time(T+2).

% :- occ(T,X,Y), not occ(T-1,X2,Y2), time(T), time(T-1), pos(X), pos(X2), pos(Y), pos(Y2), T > 3.
%:- time(T), not halting_time(T), not occ(T, X, Y), pos(X), pos(Y). 

% Non puo' essere che vado due volte sulla stessa posizione
 :- occ(T1,X,Y), occ(T2,X,Y), T1 < T2, time(T1), time(T2).
% non puo' essere che resto nella stessa posizione in T e T+2	
% :- occ(T,X,Y), occ(T+2,X,Y), time(T), time(T+2), pos(X), pos(Y).

% Non puo' essere che step non sia supportato da un candidate step
 :- step(T,X,Y), not candidateStep(T,X,Y), pos(X), pos(Y), time(T).

% Posso avere al massimo uno step per turno
0 { step(T,X,Y) : pos(X), pos(Y) } 1 :- time(T).
% 0 { occ(T,X,Y) : pos(X), pos(Y) } 0 :- {step(T,X,Y) : pos(X), pos(Y) } = 0, time(T), T > 3.

 :- occ(T, X, Y), halting_time(T), time(T), pos(X), pos(Y).

halting_time(T+2) :- time(T), {step(T,X,Y) : pos(X), pos(Y) } = 0, T > 3. 

crit(S) :- S = #min {T : halting_time(T)}, time(S).


#maximize { T@1 : crit(T) }.

#show occ/3.
#show crit/1.
%#show halting_time/1.