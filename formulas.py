#Important formulas + brief explanations

import numpy as np
import scipy as sp

#Generalized Price of Credit Risk (based on default loss distr)

avgDL = 0 #avg default loss
hurdle = 0 #hurdle rate 
VaR = 0 #VaR for each quantile
adminCosts = 0 #extra admin costs to consider

econCapital = VaR - avgDL #economic capital (rainy day)

Price = avgDL + hurdle * econCapital + adminCosts

#----------------------------------------------------------------------------------------------

#VaR of default loss function (in case below: refer to only one default loss entity
#and one quantile)
#This can be expanded further to loop for multiple credit olbigors


a = .95 #quantile. in this case, 95th.
L = 30 #default loss on single credit exposure. in this case, $30 is the total default loss for the above quantile. 

#cumulative default loss distribution function (selected upon chosen model) 
#remember, this is only for one quantile and one default loss variable only.
def cumDL(x):
    return 

VaR = cumDL(1 - a)

#----------------------------------------------------------------------------------------------
#Default loss, L, expected loss, E(L), variation of loss, var(L), volatility of loss, o_L, of default event, D (without consideration of specific quantiles)
#for a single instrument

Indicator = 0 #indicator of default event can either result in 1 (default before time T, probability p)
#or 0 (survival until time T, probability 1-p)
c = 100 #credit/amt invested. $100 in this example.
p = 0.02 #probability of default

L = c * Indicator #L is function of indicator, L(Indicator)

E_Loss = (p * c) + [(1 - p) * 0] #probability of default * L(1) + probability of survival * L(0) 

#since the other outcome is 0, then E_Loss is simplified.
E_Loss = p * c

var_L = (p * c**2) + [(1 - p) * 0**2] - E_Loss**2 #E(L^2) - E(L)^2

#simplified
var_L = (p * c**2) - E_Loss**2

o_L = np.sqrt(var_L) #volatility

#now for multiple instruments
'''
*# of cases != # of outcomes/defaults
*# of cases = 2^N

D = total defaults, N = counterparties, k = possible defaults, p = probability of default
D = summation of all indicators default value for each N (1).
N_k = Occurence to total defaults ration Given N counterparties, how many k defaults will occur 
(N!)/((N-k)!k!)
p_D = probability of each amount of default (outcome) --> p^k(1-p)^N-k
p_k = probability of observing k defaults over whole scenario --> # of outcomes * p_D --> (N!)/((N-k)!k!) * p^k(1-p)^N-k

*for simplicity's sake, p is relatively the same for all D_N (default of each N counterparty)
'''
N = 4 #4 is an example of amt of counterparties/instruments
k = np.arange(0,N,1)
D = N + 1
N_k = np.zeros(D)
p_D = np.zeros(D)
p_k = np.zeros(D)


for i in range(len(k)):
    N_k[i] = sp.special.factorial(N)/(sp.special.factorial(N - k[i])*sp.special.factorial(k[i]))

for i in range(len(k)):
   p_D[i] = p**k[i]*(1-p)**(N-k[i])

for i in range(len(k)):
    p_k[i] = N_k[i] * p_D[i]



