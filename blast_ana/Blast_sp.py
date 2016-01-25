#!/usr/bin/python
import sys
'''
python Blast_sp.py DiGluSelf.out.bln
'''
f_i = sys.argv[1]

class OrthoPara:
	def __init__(self,f):
		self.f_name = f
	def para(self):
		import re
		fh = open(self.f_name)
		f_o = self.f_name+'.para'
		fw = open(f_o,'w')
		line = fh.readline()
		count = 0
		while line:
			line = line.strip()
			mo = re.match(r'(^\w{4})(\w+.+?)\t(\w{4})',line)
			if mo:
				if mo.group(1) == mo.group(3):
					print >> fw, line
					count += 1
					print '\r',count,
			line = fh.readline()
		print 'Paralogs found'
		fh.close()
		fw.close()
        def ortho(self):
                import re
                fh = open(self.f_name)
                f_o = self.f_name+'.ortho'
                fw = open(f_o,'w')
                line = fh.readline()
                count = 0
                while line:
                        line = line.strip()
                        mo = re.match(r'(^\w{4})(\w+.+?)\t(\w{4})',line)
                        if mo:
                                if mo.group(1) != mo.group(3):
                                        print >> fw, line
                                        count += 1
                                        print '\r',count,
                        line = fh.readline()
                print 'Orthologs found'
                fh.close()
                fw.close()


obj = OrthoPara(f_i)
obj.para()
obj.ortho()
		
