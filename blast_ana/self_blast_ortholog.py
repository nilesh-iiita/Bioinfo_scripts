#!/usr/bin/python
import s_blast_stat,sys
f_i = sys.argv[1]
f_o = f_i+'.bln'
fw = open(f_o,'w')

class self_blst_ana:
	def __init__(self,f):
		self.f_name = f
	def read_f(self):
		fh = file(self.f_name)
		line = fh.readline()
		id_bit_dic = {}
		id_list = []
		while line:
			d2= {}
			line = line.strip()
			if not('#' in line):
				t_arr =  line.split('\t')
				a,b,b_s = t_arr[0],t_arr[1],t_arr[-1]
				if a not in id_list:id_list.append(a)

				if a in id_bit_dic:id_bit_dic[a][b] = b_s
				else:id_bit_dic[a] = {b:b_s}
			line = fh.readline()
		return id_bit_dic,id_list

obj = self_blst_ana(f_i)
obj.read_f()
id_bit_dic,id_list =  obj.read_f()



def var(a,b,val_arr):

	if a in id_bit_dic and b in id_bit_dic[a] and b in id_bit_dic and a in id_bit_dic[b]:
		aa = float(id_bit_dic[a][a])
		ab = float(id_bit_dic[a][b])
		ba = float(id_bit_dic[b][a])
		bb = float(id_bit_dic[b][b])
		x = ab/aa
		y = ba/bb
		m = max(x,y)
		print >> fw, a,'\t',b,'\t',m
		val_arr.append(m)
	else:
		print >> fw, a,'\t',b,'\t',0
		val_arr.append(0)
	return val_arr
	

val_arr = []
for id1 in id_list:
	for id2 in id_list:
		val_arr = var(id1,id2,val_arr)
	print id1
print 'Creating Normal-Dist plot'
s_blast_stat.summary(val_arr)
#var('BrDi_8|BRADI1G57120.1','SoBi_46|Sb09g016450.1')
