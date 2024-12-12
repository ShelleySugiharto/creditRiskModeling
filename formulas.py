#Important formulas + brief explanations

#Generalized Price of Credit Risk (based on default loss distr)

avgDL = 0 #avg default loss
hurdle = 0 #hurdle rate 
VaR = 0 #VaR for each quantile
adminCosts = 0 #extra admin costs to consider

econCapital = VaR - avgDL #economic capital (rainy day)

Price = avgDL + hurdle * econCapital + adminCosts


#VaR of default loss function (in case below: refer to only one default loss entity
#and one quantile)

a = .95 #quantile. in this case, 95th.
L = 30 #default loss. in this case, $30 is the total default loss for the above quantile

#cumulative default loss distribution function (selected upon chosen model) 
#remember, this is oly for one quantile and one default loss variable only.
def cumDL(x):
    return 

VaR = cumDL(1 - a)

