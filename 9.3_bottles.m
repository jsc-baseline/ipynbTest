clear;clc                % clears console
worth(1) = 4500000;      % value at beginning of year 1
depreciation_1 = 0.125;  % depreciation per year
depreciation_10 = 0.225; % depreciation per year after new processing
deltat = 1;              % time step: year
t = 1;                   % loop counter
while (worth(t) > worth(1) * 0.05)                                        % loops until value is less than 5% of its price
    if (t < 10)                                                           % checks year less than 10 for initial processing
        worth(t + 1) = worth(t) + deltat * -depreciation_1 * worth(t);    % computes value
    else                                                                  % checks year greater than 10 for new processing
        worth(t + 1) = worth(t) + deltat * -depreciation_10 * worth(t);   % computes value
    end                                                                   % ends check
    if (t == 7)                                                           % checks if year is 7
        worth(t + 1) = worth(t + 1) + 835000;                             % adds one-time refurbishment
    end                                                                   % ends check
    if (t == 13)                                                          % check if year is 13
        worth(t + 1) = worth(t + 1) + 37500;                              % adds minor in-service repairs 
    end                                                                   % ends check
    t = t + 1;                                                            % increments time step
end                                                                       % ends loop
fprintf("less than 5 percent of its price at beginning of year: %d\n", t) % prints result
