[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

  # Exercise 4.2
  # Generate random numbers
  random_thou = np.random.random(1000)

  # Create and plot PMF from random 1000
  pmf = thinkstats2.Pmf(random_thou)
  thinkplot.Pmf(pmf, label = 'random thousand')

  # Create and plot CDF from random 1000
  # The distribution is uniform because the cdf displays a fairly straight line
  cdf = thinkstats2.Cdf(random_thou)
  thinkplot.Cdf(cdf, label = 'random thousand')
