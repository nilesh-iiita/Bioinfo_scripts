#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
File = open(sys.argv[1]).read().splitlines()
R,data = [],[]
for i in File:
	a,b = i.split()
	R.append(a);data.append(b)

count = data
#count = (20, 35, 30, 35, 27, 30)
n_groups = len(count)
bin = np.arange(n_groups)
fig, ax = plt.subplots()
#index = np.arange(n_groups)
index = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#bar_width = 0.50
#opacity = 200
rects1 = plt.bar(index, count,  align='center')
rects1[0].set_color('#2a52be')
rects1[1].set_color('#ffbf00')
rects1[2].set_color('#9966cc')
rects1[3].set_color('#b31b1b')
rects1[4].set_color('#cd9575')
rects1[5].set_color('#915c83')
rects1[6].set_color('#008000')
rects1[7].set_color('#8db600')
rects1[8].set_color('#00ffff')
rects1[9].set_color('#4b5320')
rects1[10].set_color('#21abcd')
rects1[11].set_color('b')
rects1[12].set_color('#848482')
rects1[13].set_color('#98777b')
rects1[14].set_color('#0d98ba')
rects1[15].set_color('#8a2be2')
rects1[16].set_color('#cb4154')
rects1[17].set_color('#cd7f32')
rects1[18].set_color('#5f9ea0')
rects1[19].set_color('#e52b50')
plt.xlabel('Riboswitch Families',weight='bold')
plt.ylabel('Number of genes in Cyanobacteria sp.', weight='bold')
#plt.title('Scores by group and gender')
#plt.rc('font', weight='bold')
#plt.bar(align='center')
rects = ax.patches
#labels = ["label%d" % i for i in xrange(len(rects))]
labels = count
for rect, label in zip(rects, labels):
	height = rect.get_height()
	ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom')




plt.xticks(index, R)
plt.xticks(rotation=90, ha = 'center')#,weight='bold')
plt.legend()
plt.xlim([0,bin.size+1])

#plt.tight_layout()

fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig(str(sys.argv[1]), dpi=300)
plt.show()
