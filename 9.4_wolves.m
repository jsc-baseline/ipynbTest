clear;clc                   % clears console 
wolf(1) = 65;               % beginning of year 1 
birth = 0.065;              % natural birth rate 
death = 0.032;              % natural death rate 
bacterial_infection = 0.70; % reduces population 
deltat = 1;                 % time step: year
for t = 1:21                                                    % loops 21-year period
    wolf(t + 1) = wolf(t) + deltat * (birth - death) * wolf(t); % computes population growth
    if (mod(t, 2) != 0 && t > 1)                                % checks if year is odd
        wolf(t + 1) = wolf(t + 1) + 22;                         % wolves from neighboring Idaho 
    end                                                         % ends check
    if (mod(t, 2) == 0)                                         % checks if year is even
        wolf(t + 1) = wolf(t + 1) * (1 - bacterial_infection);  % computes population after outbreak
    end                                                         % ends check
    wolf(t + 1) = floor(wolf(t + 1));                           % makes whole wolf 
end                                                             % ends loop 
wolf(22)         % at beginning of year 22 
% plot(1:22, wolf) % plot of rabbit population as function of time for 75-year period 
 
