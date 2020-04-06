import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
headers = ['Time','Current']
df = pd.read_csv('MIC.CSV',names=headers)
print (df)


x = df['Time'] * 0.005
y = df['Current'] * 1000

# plot
plt.plot(x,y)
# beautify the x-labels
plt.xlabel('Time (s)')
plt.ylabel('Current (uA)')
plt.grid()
plt.show()