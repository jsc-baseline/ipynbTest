clear;clc      % clears console 
birth = 0.015; % interest rate 
death = 0.0;   % depreciation 
deltat = 1;    % time step 
P(1) = 6000;   % beginning of year 1 
for t = 1:11                                           % loops 11-year period 
    P(t + 1) = P(t) + deltat * (birth - death) * P(t); % computes savings balance growth 
    if (t <= 5)                                        % checks if year <= 5 
        P(t + 1) = P(t + 1) - 250;                     % withdraws $250 to pay accumulated credit card balance 
    else                                               % checks year > 5 
        P(t + 1) = P(t + 1) - 575;                     % increases withdrawal amount to $575 at end of year six and for end of all remaining years 
    end                                                % ends check 
end                                                    % ends loop 
P(12)         % at beginning of 12th year 
plot(1:12, P) % plot of account balance over time, from beginning of year 1 through beginning of year 12 
