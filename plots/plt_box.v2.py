#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import sys
from matplotlib.patches import Polygon
from collections import defaultdict

File = defaultdict(list)

F = open(sys.argv[1]).read().splitlines()
for i in F:
	ID,Val = i.split()
	File[ID].append(int(Val))
name = []
for i in File:
	name.append(i)
name.sort()
print name
data = []
for i in name:
	data.append(File[i])
numDists,N = len(name),len(name)

fig, ax1 = plt.subplots(figsize=(10, 6))
fig.canvas.set_window_title(sys.argv[1])
plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

bp = plt.boxplot(data, notch=0, sym='+', vert=1, whis=1.5)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

ax1.set_axisbelow(True)

ax1.set_xlabel('Riboswitch Families',weight='bold')
ax1.set_ylabel('Distance (nt)',weight='bold')

boxColors = ["#2a52be", "#ffbf00", "#9966cc", "#b31b1b", "#cd9575", "#915c83", "#008000", "#8db600", "#00ffff", "#4b5320", "#21abcd", "b", "#848482", "#98777b", "#0d98ba", "#8a2be2", "#cb4154", "#cd7f32", "#5f9ea0","#e52b50"]
numBoxes = numDists
medians = list(range(numBoxes))

for i in range(numBoxes):
    box = bp['boxes'][i]
    boxX = []
    boxY = []
    for j in range(5):
        boxX.append(box.get_xdata()[j])
        boxY.append(box.get_ydata()[j])
    boxCoords = list(zip(boxX, boxY))
    boxPolygon = Polygon(boxCoords, facecolor=boxColors[i])
    ax1.add_patch(boxPolygon)
    med = bp['medians'][i]
    medianX = []
    medianY = []
    for j in range(2):
        medianX.append(med.get_xdata()[j])
        medianY.append(med.get_ydata()[j])
        plt.plot(medianX, medianY, 'k')
        medians[i] = medianY[0]
    plt.plot([np.average(med.get_xdata())], [np.average(data[i])],
             color='w', marker='', markeredgecolor='k')
ax1.set_xlim(0.5, numBoxes + 0.5)
top = 1500
bottom = -500
ax1.set_ylim(bottom, top)
xtickNames = plt.setp(ax1, xticklabels=np.repeat(name, 1))
plt.setp(xtickNames, rotation=90, fontsize=8)

fig.set_size_inches(18.5, 10.5)
fig.savefig(str(sys.argv[1]+'png'), dpi=100)
plt.show()

