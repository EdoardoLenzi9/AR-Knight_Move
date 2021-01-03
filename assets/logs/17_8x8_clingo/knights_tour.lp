% -------------------------------------------------------------------------------%
%                                   DOMAINS                                      %
% -------------------------------------------------------------------------------%

pos(1..n).          % available positions (x, y coordinates on the checkerboard)  
time(1..n**2).      % turns domain


% -------------------------------------------------------------------------------%
%                                 CONSTRAINTS                                    %
% -------------------------------------------------------------------------------%

% At a certain time T, a candidateStep is a possible target for the next move
candidateStep(T,X + 2,Y + 1) :- occ(T,X,Y), time(T), pos(X + 2), pos(Y + 1), T > 1.  
candidateStep(T,X + 2,Y - 1) :- occ(T,X,Y), time(T), pos(X + 2), pos(Y - 1), T > 1.  
candidateStep(T,X + 1,Y + 2) :- occ(T,X,Y), time(T), pos(X + 1), pos(Y + 2), T > 1.  
candidateStep(T,X + 1,Y - 2) :- occ(T,X,Y), time(T), pos(X + 1), pos(Y - 2), T > 1.  
candidateStep(T,X - 1,Y + 2) :- occ(T,X,Y), time(T), pos(X - 1), pos(Y + 2), T > 1.  
candidateStep(T,X - 1,Y - 2) :- occ(T,X,Y), time(T), pos(X - 1), pos(Y - 2), T > 1.  
candidateStep(T,X - 2,Y + 1) :- occ(T,X,Y), time(T), pos(X - 2), pos(Y + 1), T > 1.  
candidateStep(T,X - 2,Y - 1) :- occ(T,X,Y), time(T), pos(X - 2), pos(Y - 1), T > 1.  

% When a step is selected (it must be a valid step) then the corresponding occ is true
occ(T+2,X,Y) :- step(T,X,Y), time(T), pos(X), pos(Y), time(T+2).

% It could never happen that a knight passes over an already-visited cell
 :- occ(T1,X,Y), occ(T2,X,Y), T1 < T2, time(T1), time(T2).
 
% It could never happen that a step is not a candidateStep
 :- step(T,X,Y), not candidateStep(T,X,Y), pos(X), pos(Y), time(T).

% For each turn the knight can do at most one step
0 { step(T,X,Y) : pos(X), pos(Y) } 1 :- time(T).

% It could never happen that after the haltingTime (last turn) a knight continues its tour
 :- occ(T, X, Y), haltingTime(T), time(T), pos(X), pos(Y).

% If at time T a knight is stalled (not a single candidateStep) then haltingTime(T) is true 
haltingTime(T+2) :- time(T), {step(T,X,Y) : pos(X), pos(Y) } = 0, T > 3. 

% Coverage is the maximization criterion = minimum haltingTime
coverage(S) :- S = #min {T : haltingTime(T)}, time(S).


% -------------------------------------------------------------------------------%
%                               SEARCH STRATEGY                                  %
% -------------------------------------------------------------------------------%

% Maximize the coverage
#maximize { T@1 : coverage(T) }.


% -------------------------------------------------------------------------------%
%                                    OUTPUT                                      %
% -------------------------------------------------------------------------------%

#show occ/3.
#show coverage/1.
%#show haltingTime/1.