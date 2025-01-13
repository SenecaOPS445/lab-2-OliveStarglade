#!/usr/bin/env python3

# Author: Olivia Melnic
# Author ID: omelnic
# Date Created: 2025/01/13

import sys

if len(sys.argv) != 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer -= 1
print('blast off!')