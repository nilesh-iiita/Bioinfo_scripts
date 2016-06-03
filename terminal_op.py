#!/usr/bin/python3

'''
Import terminal_op
Output = terminal_op.output('ls -l')
'''

__author__ = "Nilesh Kumar"
__copyright__ = "Copyright 2016, ICGEB"
__credits__ = ["N.Kumar"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Nilesh Kumar"
__email__ = "nilesh.iiita@gmail.com"
__status__ = "Educational"

import subprocess,sys
def output(cmd):
	cmd_l = cmd.split()
	output = subprocess.Popen(cmd_l, stdout=subprocess.PIPE).communicate()[0]
	output = output.decode("utf-8")
	return (output)
