#!/usr/bin/python
import glob,re
Fa_F =  glob.glob('/home/cyano/Desktop/Glutaredoxin/old/All_data_31/1_seqout/*.jacu')
GFF_F = 'GFF'
def faaoneline(fname):
        '''Takes Fasta genome file as input and returns dictionary of Fasta'''
	import re
	fh = open(fname)
	write = fname + '_oneline'
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
		fasta[head] = seq
	#print fasta
        fh.close()
        return fasta

def src_gff(File,qur):
	f = GFF_F+'/'+File+'.gff3'
	fg = open(f)
	line = fg.readline()
	while line:
		line = line.strip()
		if qur in line:
			if 'mRNA' in line:
				#print line
				return line
			if 'CDS' in line:
				return line
			if 'gene' in line:
				return line
		line = fg.readline()
	fg.close()
	
def pars_gff(line):
	if line:
		arr  = line.split()
		chrm,srt,end,srnd = arr[0],arr[3],arr[4],arr[6]
		return chrm,srt,end,srnd
	return 'NA','NA','NA','NA'

def gene_locus(line):
	mob_gene = re.match(r'(.+?)(gene:)(.+?)\s',line)
	if mob_gene:return mob_gene.group(3)
	mob_locus = re.match(r'(.+?)(locus=)(.+?)\s',line)
	if mob_locus:return mob_locus.group(3)
	if 'locus=' not in line and 'gene:' not in line:
		return line
		

for f in Fa_F:
	fa_h  = faaoneline(f)
	for ha in fa_h:
		#print len(fa_h[ha])
		temp = ha.split()
		q_f = ha[1:5]
		mob  = re.match(r'>(.+?)\|(.+?)\s(.+)',ha)
		q_ID = ''
		Pro_ID = ''
		gene_ID = ''
		abb = ''
		if mob:
			gene_ID = mob.group(3)
			Pro_ID = mob.group(2)
			q_t = mob.group(2)
			abb = mob.group(1)
			if q_t.endswith('p'):
				q_ID = q_t[:-2]
			else: q_ID  = q_t
		if not gene_ID and not Pro_ID and not abb:
			rob = re.match(r'>(.+?)\|(.+?)$',ha)
			if rob:
				Pro_ID = rob.group(2)
				gene_ID = rob.group(2)
				q_t = rob.group(2)
				abb = rob.group(1)
				q_ID = q_t
				
			
		print gene_locus(gene_ID)+'\t',abb,'\t',Pro_ID,'\t',
		#print q_ID,q_f ##########
		#print pars_gff(src_gff(q_f,q_ID))###
		for i in pars_gff(src_gff(q_f,q_ID)):
			print i+'\t',
		print len(fa_h[ha])

#test =  src_gff("ThCa",'Thecc1EG029795t1')
#print pars_gff(test)
