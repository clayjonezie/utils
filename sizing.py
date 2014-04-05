import os

if argc < 2:
   print("usage " + argv[0] + " [folder=.] [depth=1] [res=g]")

folder = '.'
depth = 1
res = 'g'

if argc >= 2:
   folder = argv[1]

if argc >= 3:
   depth = int(argv[2])

if argc >=4:
   res = argv[3]
