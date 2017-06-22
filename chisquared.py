"""
Interpreting Chi^2
Author: Sheila Kannappan
excerpted/adapted from CAP REU tutorial September 2016
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr

# experiment to illustrate Monte Carlo creation of chi^2 
# distributions for two values of N

i=0

for i in xrange(2):
    if i == 0:


        narr=30*(1+9*i) #30 first time, 300 second time
        chisqs=[]
        iters=1000  # experiment with rerunning the plots many times
             # to see how the random variations change the chi^2
             # start w/ iters=100 then change iters to 1000 and repeat

    if i == 1:
      
        narr=30*(1+9*i) 
        chisqs=[]
        iters=1000 

    for j in xrange(iters):
    # create a data set with random errors whose underlying
    # functional form is y=1/x (no free parameters in model)
        xvals = np.zeros(narr)
        yvals = np.zeros(narr)
        xvals = np.arange(narr)/(1.+9.*i) + 1.
        errs=0.1
        yvals = 1./xvals + npr.normal(0,errs,narr)  #this creates random (gaussian drawn errors)
    # what does npr.normal do?
        #draws randon samples from the gaussian (normal) distribution --- npr.normal(mu, sigma, size)

        resids = np.abs(yvals - 1./xvals)
    # why are we subtracting 1./xvals?
        #our function is y = 1/x --- since we now have errors on x, the is will give errors on y and thus the residual

        chisq = np.sum(resids**2 / errs**2)
    # roughly, how is chisq related to N?
        #the dof are equal to n-1, this is proportional to the estimated variance around the mean 
    # what if we didn't know the errors and overestimated
    # them as 0.2 -- how would chi^2 change?
        #overestimating leads to a small chi-squared: conversly underestimating leads to a large chi-squared
        chisqs.append(chisq) # building up iters trial values of chi^2
    
    if i == 0:
        redchisqdist1 = np.array(chisqs)/narr
      # compute array of "reduced chi^2" values found for 1st N
      # what does "reduced" mean? why are we dividing by narr?
          #reduced means we are diving by the dof ---  dof= number of observations - number of fitted parameters (here 0)

      
    if i == 1:
      redchisqdist2 = np.array(chisqs)/narr
      # same thing for 2nd N 
      
      
      
      
      
      
      
     


     
plt.figure(2)
plt.clf()
n1, bins1, patches1 = plt.hist(redchisqdist1,bins=round(0.05*iters),normed=1,histtype='stepfilled')
n2, bins2, patches2 = plt.hist(redchisqdist2,bins=0.05*iters,normed=1,histtype='step')
plt.setp(patches1,'facecolor','g','alpha',0.75)
plt.xlim(0,2.5)
plt.setp(patches2,'hatch','///','alpha',0.75,color='blue')
# what good plotting strategies are being used here?
    #overplotting - use differnet colors, transparencys to see the graph

plt.title('comparison of reduced chi-squared distributions')
#plt.title('reduced chi-squared distribution') 
# switch titles above when you add N=300 case

plt.text(1.4,1,"N=30",size=11,color='g')
plt.text(1.2,3,"N=300",size=11,color='b')


# Q: how can we determine the confidence level associated with
#    a certain deviation of reduced chi^2 from 1?
# A: we have to do the integral under the distribution --
#    e.g. for 3sigma (99.8%) confidence find x such that
#    the integral up to x contains 99.8% of the area
# how can you approximate this using np.argsort?
# make sure to set iters=1000 for this exercise....

### where  .998*N/2     
"""
inds=redchisqdist1[np.where(np.argsort(redchisqdist1) == 30)]


print(inds) # fill in to print red. chi^2 for 99.8% conf. for N=30



inds=redchisqdist1[np.where(np.argsort(redchisqdist1) == 30)]
print(inds) # fill in to print red. chi^2 for 99.8% conf. for N=300
# look at the graph and verify your answers make visual sense
"""

inds=np.argsort(redchisqdist1)
print("Red. Chi^2 for 99.8% conf. for N=30:") # fill in to print red. chi^2 for 99.8% conf. for N=30
print(redchisqdist1[inds[998]])
inds=np.argsort(redchisqdist2)
print("Red. Chi^2 for 99.8%% conf. for N=300:") # fill in to print red. chi^2 for 99.8% conf. for N=300
print(redchisqdist2[inds[998]])
