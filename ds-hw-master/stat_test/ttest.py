from math import sqrt

from scipy.stats import t
from numpy import mean

def degrees_of_freedom(s1, s2, n1, n2):
    """
    Compute the number of degrees of freedom using the Satterhwaite Formula
    
    @param s1 The unbiased sample variance of the first sample
    @param s2 The unbiased sample variance of the second sample
    @param n1 Thu number of observations in the first sample
    @param n2 The number of observations in the second sample
    """
    result = ((float(s1) / n1) + (float(s2) / n2))**2 / ((float(s1) / n1)**2 / (n1 - 1) + (float(s2) / n2)**2 / (n2 - 1))
    return result

def unbiased_sample_variance(observations, mean):
    """
    Compute the unbiased sample variance

    @param observations Iterable set of observations
    @param mean The estimated mean
    """
    result = 0
    for var in observations:
        result += (var - mean)**2
    result /= len(observations) - 1
    return result

def t_statistic(mean1, mean2, n1, n2, svar1, svar2):
    """
    Compute the t-statistic for the given estimates
    """
    result = (mean1 - mean2) / sqrt((svar1 / n1 + svar2 / n2))
    return result

def t_test(sample1, sample2):
    """
    Return the two-tailed p-value of a t test with unequal variance for two samples.

    @param sample1 An iterable of the first sample
    @param sample2 An iterable of the second sample
    """
    s1 = unbiased_sample_variance(sample1, mean(sample1))
    s2 = unbiased_sample_variance(sample2, mean(sample2))
    degrees = degrees_of_freedom(s1, s2, len(sample1), len(sample2))
    t_value = t_statistic(mean(sample1), mean(sample2), len(sample1), len(sample2), s1, s2)
    result = 1 - t.cdf(t_value, max(len(sample1) - 1, len(sample2) - 1))
    return result * 2

if __name__ == "__main__":
    v1 = [5, 7, 5, 3, 5, 3, 3, 9]
    v2 = [8, 1, 4, 6, 6, 4, 1, 2]

    print("p-value is %f" % t_test(v1, v2))
