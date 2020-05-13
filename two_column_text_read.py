# Read first two columns
import numpy as np
import matplotlib.pyplot as plt


while True:
    try:
        infile = open('filename', 'r')  # filename is the name of the file
        break
    except OSError:
        print("File not found, please choose different file")


x = []  # column 1
y = []  # column 2


for line in infile:
    content = line.split()  # two columns split up to read
    x.append(content[0])
    y.append(content[1])
infile.close()
print(x)
print(y)


x, y = np.array(x), np.array(y)
plt.plot(x, y, color='blue', linewidth=1.5)
plt.xlabel('value of x')
plt.ylabel('value of y')
plt.show()

exit