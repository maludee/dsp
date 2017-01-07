[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

# Exercise 3.1
# Read the data from the respondent file
%matplotlib inline
import chap01soln
resp = chap01soln.ReadFemResp()

# Create the pmf of of numkdhh, the number of children under 18 in the respondent's household.
import thinkstats2
import thinkplot
pmf = thinkstats2.Pmf(resp.numkdhh)

# Make the pmf
thinkplot.Pmf(pmf, label = 'numkdhh')

# Define biaspmf using author code
def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

# Make a the biased Pmf of children in the household if you surveyed the children.
biased_pmf = BiasPmf(pmf, label = 'observed')

# Display the actual Pmf and the biased Pmf on the same axes.
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel = 'children', ylabel = 'PMF')

# Compute the means of the pmf and biased pmf
print (pmf.Mean())
print (biased_pmf.Mean())
