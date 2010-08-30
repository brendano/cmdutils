#!/usr/bin/env python
"""Set operations on files as lists.  Symlink as:
    setdiff [-c] <set1> <set2> - set difference
    setand  [-c] <set1> <set2> - set intersection
    setor   [-c] <set1> <set2> - set union
-c : only give count of the result.

Output order is randomish
We don't newline chomp, so a bug if your file doesnt end with a newline 
Dash - for stdin (e.g. cut/awk/sed/grep)
Though in zsh, =(cmd) syntax is superior: can do 2 pipeline inputs
(The <(cmd) syntax is always buggy for me.)
brendan o'connor - anyall.org/setdiff.py
"""

# wget anyall.org/setdiff.py; for x in diff and or;do ln -s setdiff.py set$x; done

from __future__ import division
import sys
do_count = False
if '-c' in sys.argv:
  sys.argv.pop( sys.argv.index('-c') )
  do_count = True
if len(sys.argv) == 1:
  print __doc__.strip()
  sys.exit(1)
file1,file2 = sys.argv[1], sys.argv[2]
file1 = sys.stdin if file1=='-' else open(file1)
file2 = sys.stdin if file2=='-' else open(file2)
if file1==file2==sys.stdin: raise Exception("can't both be stdin")
set1,set2 = set(file1), set(file2)
cmdname = sys.argv[0].split("/")[-1].replace(".py","")
if cmdname == 'setdiff':   result = set1 - set2
elif cmdname == 'setand':  result = set1 & set2
elif cmdname == 'setor':   result = set1 | set2
else: raise Exception("bad command name")

if do_count:
  print len(result)
else:
  for l in result:  print l,
