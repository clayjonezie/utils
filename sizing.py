#wraps du with proper defaults

import os, sys

argc = len(sys.argv)

folder = '.'
depth = 1
res = 'g'

if argc >= 2:
   folder = sys.argv[1]

if argc >= 3:
   depth = sys.argv[2]

if argc >=4:
   res = sys.argv[3]

command = "du -d " + str(depth) + " -" + res + " " + folder

os.system(command)
