#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np

from collections import defaultdict

File = defaultdict(list)

F = open('data.txt').read().splitlines()
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
#print data
plt.boxplot(data, 0, 'gD')
#plt.figure()
plt.show()

