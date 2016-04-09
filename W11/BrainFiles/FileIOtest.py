__author__ = 'HanWei'
fin = open('C:\Users\HanWei\Dropbox\SUTDNotes\SUTDTerm3\\2D\DW2DShenanigans.txt','a')
# fin.write('hi\n')
# fin.write('bye\n')
import urllib2
req = urllib2.Request('http://people.sutd.edu.sg/~oka_kurniawan/10_009/y2015/2d/tests/level1_1.inp')
req.add_header('User-agent', 'SUTD 2D Demo')
res = urllib2.urlopen(req)

destination = []
for line in res:
    destination.append(line.strip())