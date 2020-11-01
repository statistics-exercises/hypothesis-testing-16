import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_statistic(self) : 
        for n in range(1,21) :
            mu, sigma = -10 +n, 0.1*n
            samples = np.random.normal(mu, sigma, size=20*n )
            stat = ( sum(samples) / (20*n) - mu ) / ( sigma / np.sqrt(n*20) )
            self.assertTrue( np.abs( stat - testStatistic( samples, mu, sigma) )<1e-7, "your function for computing the test statistic is not working correctly" )
            
    def test_pvalue(self) : 
        for n in range(1,21) :
            mu, sigma = -10 +n, 0.1*n
            samples = np.random.normal(mu, sigma, size=20*n )
            stat = testStatistic( samples, mu, sigma )
            pval = 1 - scipy.stats.norm.cdf(stat)
            self.assertTrue( np.abs( pval - pvalue( samples, mu, sigma ) )<1e-7, "your function for computing the pvalue is not working correctly" )

        stat = testStatistic( data, 3, 4 )
        pval = 1 - scipy.stats.norm.cdf(stat)
        self.assertTrue( np.abs( pval - pvalue( data, 3, 4 ) )<1e-7, "your function for computing the pvalue is not working correctly" )
        
    def test_pvalue2(self) : 
        stat = testStatistic( data, 3, 4 )
        pval = scipy.stats.norm.cdf(stat)
        self.assertFalse( np.abs( pval - pvalue( data, 3, 4 ) )<1e-7, "The alternative hypothesis for this test is that the statistic is greater than the value that is given for in the statement of the null hypothesis.  The critical region would thus be all values greater than some value" )
