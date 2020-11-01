import numpy as np
import scipy.stats

def testStatistic( data, mu, sigma ) : 
  # Your code to compute the testStatistic that is described
  # in the text on the right should be calculated here
  
  
def pvalue( data, mu, sigma ) :
  T = testStatistic(data, mu, sigma)
  # You should add code here that uses the T value that is returned from 
  # testStatistic to determine the p-value for the hypothesis test.
  

# The code from here should not need to be modified
data = np.loadtxt("mydata.dat")
print("The null hypothesis is that the data is a set of samples from a distribution")
print("with an expectation of 3")
print("The alternative hypothsis is that the data is a set of samples from a distribution")
print("with an expectation that is greater than 3")
print("The p-value for this hypothesis test is", pvalue(data, 3, 4) )
