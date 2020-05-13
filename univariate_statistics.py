import numpy as np
data = np.array([[1.0,2.0],[3.0,4.0]])
while True:
    try:
        x = data[0]
        y = data[1]
        break
    except IndexError:
        print('Data Array has an unreasonable amount of dimensions, to proceed use only two dimensions')

#Mean
mean2 = sum(y)/len(y)

print('The second examples mean is:', mean2)
#Standard Deviation
variance2 = sum([((float(i) - mean2)**2) for i in y])/len(y)
res2 = variance2**0.5
print("Standard deviation for the second example is: " + str(res2))

#Max and Min
maxx= max(x)
print(maxx)
maxy = max(y)
print(maxy)

minx = min(x)
print(minx)
miny = min(y)
print(miny)

values = np.array([mean2, res2, maxx, minx, maxy, miny])
print(values)