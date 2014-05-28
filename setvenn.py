#!/usr/bin/env python
"""setvenn [opts] <set1> <set2>
Venn diagram overview of two files as sets.  
Show interesting counts and Jaccard ratio.
-s : Show items of the set differences.

We don't newline chomp, so a bug if your file doesnt end with a newline 
Dash - for stdin (e.g. cut/awk/sed/grep)
or try <(cmd) or =(cmd) shell syntax

EXAMPLE

  $ setvenn list1.txt list2.txt
    |A| =    28   |A&B| =    22     |B| =    22
  |A-B| =     6   |AvB| =    28   |B-A| =     0
     AB/A 0.786    Jacc = 0.786      AB/B 1.000

  $ setvenn -s list1.txt list2.txt 
    |A| =    28   |A&B| =    22     |B| =    22
  |A-B| =     6   |AvB| =    28   |B-A| =     0
     AB/A 0.786    Jacc = 0.786      AB/B 1.000

  ***  |A-B| =  6  ***
  APW_ENG_20030122.0094.ann
  APW_ENG_19960124.0119.ann
  APW_ENG_20030803.0091.ann
  APW_ENG_19960322.0777.ann
  APW_ENG_20081024.0398.ann
  APW_ENG_20001229.0811.ann

  ***  |B-A| =  0  ***
"""

from __future__ import division
import sys

show_items=False
if '-s' in sys.argv:
  sys.argv.pop( sys.argv.index('-s') )
  show_items = True
if len(sys.argv) != 3 or '-h' in sys.argv:
  print __doc__.strip()
  sys.exit(1)

file1,file2 = sys.argv[1], sys.argv[2]
file1 = sys.stdin if file1=='-' else open(file1)
file2 = sys.stdin if file2=='-' else open(file2)
if file1==file2==sys.stdin: raise Exception("can't both be stdin")
a,b = set(file1), set(file2)
_and = a & b
_or  = a | b
w = len(str(len(_or)))
w = max(w, 5)
print "  |A| = %*d   |A&B| = %*d     |B| = %*d" % (w,len(a), w,len(_and), w,len(b))
print "|A-B| = %*d   |AvB| = %*d   |B-A| = %*d" % (w,len(a-b), w,len(_or), w,len(b-a))
print "   AB/A %-*.3f    Jacc = %-*.3f      AB/B %-*.3f" % (
    w,len(_and)/len(a) if len(a) else float('nan'),
    w,len(_and)/len(_or) if len(_or) else float('nan'),
    w,len(_and)/len(b) if len(b) else float('nan'))
if show_items:
  print "\n***  |A-B| = %2d  ***" % (len(a-b),)
  for x in (a-b): print x,
  print "\n***  |B-A| = %2d  ***" % (len(b-a),)
  for x in (b-a): print x,
