#-----------------------------------------------------------------------
# powersoftwo.py
#-----------------------------------------------------------------------

import sys

# Accept positive integer n as a command-line argument. Write to
# standard output a table showing the first n powers of two.

n = int(sys.argv[1])

power = 1
i = 0
while i <= n:
    print(str(i) + ' ' + str(power))
    power = 2 * power
    i = i + 1

#-----------------------------------------------------------------------

# python powersoftwo.py 0
# 0 1

# python powersoftwo.py 1
# 0 1
# 1 2

# python powersoftwo.py 2 
# 0 1
# 1 2
# 2 4

# python powersoftwo.py 3
# 0 1
# 1 2
# 2 4
# 3 8

# python powersoftwo.py 4
# 0 1
# 1 2
# 2 4
# 3 8
# 4 16


Copyright © 2000–2015, Robert Sedgewick, Kevin Wayne, and Robert Dondero.
Last updated: Fri Oct 20 20:45:16 EDT 2017.
