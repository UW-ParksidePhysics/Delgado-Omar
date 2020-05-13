import sys

from numpy import array, polyval, linspace

def fit_curve_array(fit_eos, minimum_x, maximum_x):

    try:
    x = linspace(minimum_x, maximum_x)
    y = fit_eos
    fit_curve = array([x, y])
    return fit_curve

    except ArithmeticError:
    print('ArithmeticError: Error. Please try again with something that works.')
    except IndexError:
    print('Error. Please try another way')