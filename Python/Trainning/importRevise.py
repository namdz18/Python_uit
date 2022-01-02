from revise import *
import numpy as np
import matplotlib.pyplot as plt

x = analyze_training_database('6')
#number of bar
xpoints = np.array(x[0])
#value(height) of bar
ypoints = np.array(x[1])
apoints = np.array(x[2])
bpoints = np.array(x[3])
zpoints = np.array(x[4])
plt.bar(xpoints, ypoints, color = 'red', label = 'Max')
plt.bar(xpoints, apoints, color = 'green', label = 'Min')
plt.bar(xpoints, bpoints, color = 'black', label = 'Average')
plt.bar(xpoints, zpoints, color = 'yellow', label = 'Median')
plt.title("Barchart about special values of each class")
#setup value on bar
# for i in range(0, len(x[0])):
#     plt.text(i, ypoints[i], round(ypoints[i], 5), ha = "center", va = "bottom") #ha: horizontal alignment; va: vertical alignment
# for i in range(0, len(x[0])):
#     plt.text(i, apoints[i], round(apoints[i], 5), ha = "center", va = "bottom") #ha: horizontal alignment; va: vertical alignment
# for i in range(0, len(x[0])):
#     plt.text(i, bpoints[i], round(bpoints[i], 5), ha = "center", va = "bottom") #ha: horizontal alignment; va: vertical alignment
# for i in range(0, len(x[0])):
#     plt.text(i, zpoints[i], round(zpoints[i], 5), ha = "center", va = "bottom") #ha: horizontal alignment; va: vertical alignment
plt.legend()
plt.show()