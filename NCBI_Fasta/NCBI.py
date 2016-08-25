#!/usr/bin/python

__author__ = "Nilesh Kumar"
__email__ = "nilesh.iiita@gmail.com"

import urllib2,sys

List = open(sys.argv[1]).read().splitlines()
for gi in List:
        url = 'https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?tool=portal&sendto=on&log$=seqview&db=protein&dopt=fasta&sort=&val='+gi+'&from=begin&to=end&maxplex=1'
        resp = urllib2.urlopen(url)
        page = resp.read()
        print (page),
