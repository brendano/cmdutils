#!/usr/bin/env python
"""setvenn  <set1> <set2>
Venn diagram overview of two files as sets.  
Show interesting counts and Jaccard ratio.
-s : Show items of the set differences.

We don't newline chomp, so a bug if your file doesnt end with a newline 
Dash - for stdin (e.g. cut/awk/sed/grep)
Though in zsh, =(cmd) syntax is superior: can do 2 pipeline inputs
"""

from __future__ import division
import sys
show_items=False
if '-s' in sys.argv:
  sys.argv.pop( sys.argv.index('-s') )
  show_items = True
if len(sys.argv) == 1:
  print __doc__.strip()
  sys.exit(1)
file1,file2 = sys.argv[1], sys.argv[2]
file1 = sys.stdin if file1=='-' else open(file1)
file2 = sys.stdin if file2=='-' else open(file2)
if file1==file2==sys.stdin: raise Exception("can't both be stdin")
a,b = set(file1), set(file2)
cmdname = sys.argv[0].split("/")[-1].replace(".py","")
_and = a & b
_or  = a | b
w = len(str(len(_or)))
w = max(w, 5)
print "  |A| = %*d   |A&B| = %*d     |B| = %*d" % (w,len(a), w,len(_and), w,len(b))
print "|A-B| = %*d   |AvB| = %*d   |B-A| = %*d" % (w,len(a-b), w,len(_or), w,len(b-a))
print "   AB/A %-*.3f    Jacc = %-*.3f      AB/B %-*.3f" % (w,len(_and)/len(a), w,len(_and)/len(_or), w, len(_and)/len(b))
if show_items:
  print "\n***  |A-B| = %*d  ***" % (w,len(a-b),)
  for x in (a-b): print x,
  print "\n***  |B-A| = %*d  ***" % (w,len(b-a),)
  for x in (b-a): print x,
sys.exit()
