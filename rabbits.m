clear;clc                % clears console 
birth = 0.2;             % percentage per year birth rate 
death = 0.0;             % negligible death rate 
death_by_disease  = 0.8; % deadly disease occurs when rabbit population > 300 
deltat = 1;              % time step 
P(1) = 100;              % beginning of year 1 
for t = 1:75                                          % loops 75-year period 
    P(t + 1) = P(t) + deltat * (birth) * P(t);        % computes population growth 
    if (P(t + 1) > 300)                               % checks if rabbit polulation > 300 
        P(t + 1) = P(t + 1) * (1 - death_by_disease); % computes population after outbreak 
    end                                               % ends check 
    P(t + 1) = floor(P(t + 1));                       % makes whole rabbit 
end                                                   % ends loop 
P(76)         % at beginning of year 76 
plot(1:76, P) % plot of rabbit population as function of time for 75-year period 
 
