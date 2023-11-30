import schedule
import scrapper
import random
import time
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

#schedule.every(1).minutes.do()

def replTest():
    
    t1 = datetime.now().time()
    t11 = t1.second + ((t1.microsecond)/1000000)
    x = 0
    while x != 6:
        x = random.randint(1, 6)
        time.sleep(0.1)

    t2 = datetime.now().time()
    t22 = t2.second + ((t2.microsecond)/1000000)
    t = t22 - t11
    return(np.abs(t))

moyennes = []
for k in range (0,10):
    for i in range(0,10):
        times = []
        times.append(replTest())
    moyennes.append(np.average(times))

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

y = np.array(moyennes)
x = np.arange(0, 10)

plt.title("Line graph")
plt.bar(x,y, width=0.08, edgecolor='None',color='k',align='center')

plt.show()




