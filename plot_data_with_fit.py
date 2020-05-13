def plot_data_with_fit(data, fit_curve, format_x, format_y):
    import matplotlib.pyplot as plt
    import numpy as np

    import matplotlib.pyplot as mp
    mp.title('Final Curve Plot')
    format_x
    format_y

    plt.scatter(data[0],data[1],  label='Data', s=1,)
    plt.plot(fit_curve[0],fit_curve[1], 'blue')
    return plt.show()
