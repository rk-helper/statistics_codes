#### Shity code to find point with ci percentage

from scipy.stats import norm
from scipy.stats import chi2
from scipy.stats import t

x = str(input('Type of distirbution: '))  # type of distirbution
n = int(input('Type percentage of ci interval: '))  # Type percentage of ci interval
if x == 'norm':
    print('left point:', norm.ppf(((100 - n) / 2) / 100))
    print('right point:', norm.ppf((((100 - n) / 2) + n) / 100))
elif x == 'chi2':
    df = int(input('Degrees of freedom of chi2: '))  # number of experiments
    print('left point:', chi2.ppf(((100 - n) / 2) / 100, df - 1))
    print('right point:', chi2.ppf((((100 - n) / 2) + n) / 100, df - 1))
elif x == 't':
    df = int(input('Degrees of freedom of t: '))  # number of experiments
    print('left point:', t.ppf(((100 - n) / 2) / 100, df - 1))
    print('right point:', t.ppf((((100 - n) / 2) + n) / 100, df - 1))
