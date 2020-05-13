import sys

def quadratic_fit(data):
    from numpy import polyfit

    un_data = zip(*data)
    data_2 = list(un_data)

    x = data[0]
    y = data[1]
    quadratic_coefficients = polyfit(data[0], data[1], 2)
    return quadratic_coefficients

