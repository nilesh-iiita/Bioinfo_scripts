#!/usr/bin/python
import sys,re
def faaoneline(fname):
        '''python fasta_online.py Fasta.fa'''
	import re
	fh = open(fname)
	#write = fname + '_oneline'
        #fw = open(write,'w')
	Lines = fh.readlines()
	head = ''
	seq = ''
        fasta = {}
        for line in Lines:
		line = line.strip()
		if line.startswith('>'):
			#print >>fw,line
			head = line
                        seq = ''
		if not line.startswith('>'):
			line = line.strip()
			seq += line
		#fasta = {'head':head,'seq':seq};
		#fasta = {'head':head,'seq':seq};
		#print >>fw,seq
		fasta[head] = seq
	#print fasta
        fh.close()
       # fw.close()
        return fasta

def CXXC(seq,head):
	#print seq
	#matchobj = re.match(r'(SYCPYCVKVKDL)',seq)
	#@if matchobj:
	#	print matchobj.group()
	#else:
	#	print "No match!!"
	#line = seq
	I=[m.start() for m in re.finditer('(?=C..C)', seq)]
	#print head
	#for i in I:
	#	print seq[i:i+4],i,i+4
	if I:
		return 1
	else: 
		return 0
def CCXC(seq,head):
        #print seq
        #matchobj = re.match(r'(SYCPYCVKVKDL)',seq)
        #@if matchobj:
        #       print matchobj.group()
        #else:
        #       print "No match!!"
        #line = seq
        I=[m.start() for m in re.finditer('(?=CC.C)', seq)]
        #print head
        #for i in I:
        #       print seq[i:i+4],i,i+4
        if I:
                return 1
        else:
                return 0


def CGFS(seq,head):
        #print seq
        #matchobj = re.match(r'(SYCPYCVKVKDL)',seq)
        #@if matchobj:
        #       print matchobj.group()
        #else:
        #       print "No match!!"
        #line = seq
        I=[m.start() for m in re.finditer('(?=CGFS)', seq)]
	#print head
        #for i in I:
        #       print seq[i:i+4],i,i+4,
        if I:
                return 1
        else:
                return 0
def bothch(seq,head):
	I=[m.start() for m in re.finditer('(?=C..C)', seq)]
	L=[m.start() for m in re.finditer('(?=CGFS)', seq)]
	#for i in I:
	#	print 'CGFS',head,seq[i:i+4],i,i+4
	if I:
		for i in L:
			#print #for i in I:
			print head,seq[i:i+4],i,i+4
	if L:
                for i in I:
                        #print #for i in I:
                        print head,seq[i:i+4],i,i+4





fname = sys.argv[1]
fasta = faaoneline(fname)
cxxc = [] #di
ccxc = [] #di2
cgfs = [] #mono
other = []
both = []
#seq = 'VVVFSK-SYCPYCVKVKDL-LKKLGAKFIAVELDK--E-S-D-G-AQVQS-------ALAE-WT----------------------------G------Q--RTVPNVFIGEKHI'

for head in fasta:
	if CXXC(fasta[head],head) and not  CGFS(fasta[head],head):
		if head not in cxxc: 
			cxxc.append(head)
		#print head
		#if 'ArTh' in head:
		#	print 'cxxc',head
	if CCXC(fasta[head],head) and not  CGFS(fasta[head],head):
                if head not in ccxc:
                        ccxc.append(head)
                #print head
                #if 'ArTh' in head:
                #       print 'cxxc',head

	if CGFS(fasta[head],head) and not CXXC(fasta[head],head):
		if head not in cgfs:
                	cgfs.append(head)
		#print head
		#if 'ArTh' in head:
                #        print 'cgfs',head
	else:

		if (CXXC(fasta[head],head) and CGFS(fasta[head],head)):
			both.append(head)
			if 'ArTh' in head:
                        	print 'both',head
		if not CXXC(fasta[head],head) and not CGFS(fasta[head],head):
        	        other.append(head)
			#print head
			#if 'ArTh' in head:
                        #	print 'other',head
#print both


otherdic = {}
for h in other:
	#print h[1:5]
	if h[1:5] not in otherdic:
		otherdic[h[1:5]] = 1
	else:
		otherdic[h[1:5]] += 1

bothdic = {}
for h in both:
        #print h[1:5]
        if h[1:5] not in bothdic:
                bothdic[h[1:5]] = 1
        #if h[1:5] in bothdic:
	else:
                bothdic[h[1:5]] += 1


didic = {}
for h in cxxc:
        
        if h[1:5] not in didic:
                didic[h[1:5]] = 1
        #if h[1:5] in didic:
	else:
                didic[h[1:5]] += 1

didic2 = {}
for h in ccxc:

        if h[1:5] not in didic2:
                didic2[h[1:5]] = 1
        #if h[1:5] in didic:
        else:
                didic2[h[1:5]] += 1


monodic = {}
for h in cgfs:
        #print h[1:5]
        if h[1:5] not in monodic:
                monodic[h[1:5]] = 1
        #if h[1:5] in monodic:
	else:
                monodic[h[1:5]] += 1


alldic={}
for ids in fasta:
	#if 'ArTh' in head:
	#print head
	i = ids[1:5]
	if i not in alldic:
		alldic[i] = 1
	else:
		alldic[i] += 1
#print '>>>>>>>>>>>>> ALL >>>>>>>>>>>>>>>>>>>>>'

#for ids in fasta:
#	if 'ArTh' in ids:
#		print ids


print 'ID\tall\tCGFS\tCXXC\tCCXC\tC(C|X)XC\tboth\tother\tm+d+o\tdiff'
listid = []
for i in alldic:
	listid.append(i)
#print listid
listid.sort()
#print listid

#print alldic['ArTh']
for id in listid:
	m,d,b,o = 0,0,0,0
	##print id,monodic[id],didic[id],other[id]
	print id,'\t',alldic[id],'\t',

	if id in monodic:
		##print monodic[id],
		m = monodic[id]
	if id not in monodic:
		##print 0,
		m = 0

	if id in didic:
                ##print didic[id],
		d  = didic[id]
        if id not in didic:
                ##print 0,
		d = 0
	
	if id in didic2:
                ##print didic[id],
                d2  = didic2[id]
        if id not in didic2:
                ##print 0,
                d2 = 0

	if id in bothdic:
                ##print didic[id],
                b  = bothdic[id]
        if id not in bothdic:
                ##print 0,
                b = 0


	if id in otherdic:
                ##print otherdic[id],
		o = otherdic[id]
        if id not in otherdic:
                ##print 0, 
		o  = 0
	if id not in alldic:
		print 0,'\t',
		

	print m,'\t',d-d2,'\t',d2,'\t',d,'\t',b,'\t',o,'\t',m+d+b+o,'\t',m+d+b+o-alldic[id]


#print didic['JaCu']	
